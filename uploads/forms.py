from django import forms

from models import UploadedFile

class FormUploadFile(forms.ModelForm):
    class Meta:
        model = UploadedFile
        exclude = ('content_type','object_id')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)

        super(FormUploadFile, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        upfile = super(FormUploadFile, self).save(False)

        upfile.owner = self.owner
        upfile.save()

        return upfile
