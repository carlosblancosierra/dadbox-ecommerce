import datetime
import os

AWS_GROUP_NAME = "Python_eCommerce_Group"
AWS_USERNAME = "python-ecommerce-user"
# AWS_ACCESS_KEY_ID = "AKIAIBVDPHHLO6H2AGYQ"
# AWS_SECRET_ACCESS_KEY = "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"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID","AKIAIBVDPHHLO6H2AGYQ")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY","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")


AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'ecommerce.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'ecommerce.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'dadbox-python-ecommerce'
S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

# AWS_QUERYSTRING_AUTH = True