from django.conf import settings

UPLOADS_PATH = getattr(settings, 'UPLOADS_PATH', 'uploads')
