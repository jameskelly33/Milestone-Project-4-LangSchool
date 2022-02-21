from django.conf import settings
from storages.backends.sboto3 import S3Boto3Storage


class StaticStorages(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION



class MediaStorages(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION