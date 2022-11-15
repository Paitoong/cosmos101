import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://XXXXXXXXX.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'XXXXXXXXXX'),
    'database_id': os.environ.get('COSMOS_DATABASE', 'MyDatabase'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Employees'),
}
