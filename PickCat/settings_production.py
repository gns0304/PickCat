import os

SECRET_KEY = os.environ.get['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['*']

from .storage_config import *