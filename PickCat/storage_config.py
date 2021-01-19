import os

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']
AWS_S3_REGION_NAME = os.environ['S3_REGION']
AWS_ACCESS_KEY_ID = os.environ['S3_ID']
AWS_SECRET_ACCESS_KEY = os.environ['S3_KEY']
AWS_QUERYSTRING_AUTH = False
AWS_S3_ENDPOINT_URL = os.environ['S3_ENDPOINT']
AWS_S3_ADDRESSING_STYLE = 'virtual'