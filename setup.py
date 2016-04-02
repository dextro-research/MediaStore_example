from setuptools import setup

app_config = {
    'name': "mediastore",
    'version': "0.0.1",
    'author': "Dextro",
    'author_email': "team@dextro.co",
    'description': "Media Store example service",
    'packages': ["mediastore"],
    'include_package_data': True,
    'zip_safe': False,
    'install_requires': [ 
        "Flask==0.10.1",
        "boto==2.37.0",
        "Jinja2==2.7.3",
        "redis==2.10.3",
        "requests==2.9.1",
        "SQLAlchemy",
        "Flask-SQLAlchemy",
        "psycopg2",
        "Flask-Migrate==1.7.0"
    ],
    'url': "https://github.com/dextro-research/MediaStore_example"
}

setup(**app_config)