import os


__version__ = '0.0.1'

DATABASE_URL = os.getenv('POSTGRES_URL', 'postgresql://root:secret_password@127.0.0.1/data')
