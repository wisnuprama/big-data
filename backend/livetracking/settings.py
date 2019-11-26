import os

# config
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'hehehe')
IS_DEVELOPMENT = os.getenv('FLASK_ENV', 'development') == 'development'

# web server
HOST = '0.0.0.0'

# datasource
DATABASE = {
    'keyspace': {
        'name': 'livetracking',
        'replication_factor': 1 if IS_DEVELOPMENT else 2,
    },
    'config': {
        'default_keyspace': 'livetracking',
        'hosts': ['172.21.128.1',],
        'retry_connect': True,
        'port': 9042
    }
}