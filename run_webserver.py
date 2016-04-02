from mediastore import app
import os

if __name__ == '__main__':
    env = os.getenv('ENVIRONMENT')
    if env == 'Development':
        app.run(host="0.0.0.0", port=3001, debug=True)
    else:
        app.run(host="0.0.0.0", port=80, debug=False)