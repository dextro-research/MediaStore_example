from mediastore import app, db
from math import ceil
import random
from time import sleep
from mediastore.models import Media, Entity
from flask import jsonify, request


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Media Store', 'status': 'success'})


@app.route('/media', methods=['POST'])
def add_media():
    payload = request.get_json()
    required_fields = ['media_url', 'entities']
    
    clean_payload = {}
    for field in required_fields:
        try:
            clean_payload[field] = payload[field]
        except KeyError:
            return jsonify({'message': "Missing required field {}".format(field), 'status': 'error'})
    
    # Cast the entities into a list if they aren't already
    if not isinstance(clean_payload['entities'], list):
        clean_payload['entities'] = [clean_payload['entities']]
    
    #Let's guarentee uniqueness in entities
    clean_payload['entities'] = set([e.lower() for e in clean_payload['entities']])
    
    # before we grab the media, we would need to download it, and transfer it - 
    # instead of dealing with actual media, let's use a short sleep
    sleep(random.randint(1,5))
    
    media = Media.query.filter(Media.media_url == clean_payload['media_url']).first()
    if not media:
        media = Media(media_url = clean_payload['media_url'])
        db.session.add(media)
        
    current_entities = set([e.label for e in media.entities])
    
    for entity_label in clean_payload['entities']:
        try:
            entity_label = str(entity_label)
        except:
            # Something not a string was passed, so abort this entity creation
            continue
        
        # Make sure we skip duplicates
        if entity_label in current_entities:
            continue
        
        entity = Entity.query.filter(Entity.label == entity_label).first()
        if not entity:
            
            entity = Entity(label = entity_label)
            db.session.add(entity)
        
        entity.media.append(media)
        
    
    db.session.commit()
    
    return jsonify({'status': 'success', 'data': _serialize_media(media)})
    
    

    
@app.route('/media', methods=['GET'])
def get_media_for_entity():
    page = int(request.args.get('page', 1))
    limit = 100
    total = Media.query.count()
    media = Media.query.order_by(Media.created_at).offset((page - 1) * limit).limit(limit)
    
    return jsonify({'status': 'success',
                    'data': [_serialize_media(m) for m in media],
                    'total': total,
                    'total_pages': int(ceil(total / limit)),
                    'current_page': page})
    
        

        
def _serialize_media(media):
    print media.entities
    return { 'id': media.id,
             'media_url': media.media_url,
             'entities': [e.label for e in media.entities]}    