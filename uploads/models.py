from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

import app_settings

class UploadedFileManager(models.Manager):
    def get_by_owner(self, owner):
        ctype = ContentType.objects.get_for_model(owner.__class__)

        return self.get_query_set().filter(
                content_type=ctype,
                object_id=owner.id,
                )

class UploadedFile(models.Model):
    """Stores an uploaded file to attach to any object on database"""
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=app_settings.UPLOADS_PATH)

    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    owner = generic.GenericForeignKey('content_type','object_id')

    objects = UploadedFileManager()

    def __unicode__(self):
        return self.title or self.file.path
