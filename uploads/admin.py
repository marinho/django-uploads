from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import UploadedFile

admin.site.register(UploadedFile)
