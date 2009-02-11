from django import template

from uploads.models import UploadedFile

register = template.Library()

@register.filter
def has_uploaded_files(obj):
    """Returns True or False if there are uploaded files that the owner object
    is the given object"""
    
    return bool(UploadedFile.objects.get_by_owner(obj).count())

class UploadedFilesByOwnerNode(template.Node):
    obj = None
    as_varname = None

    def __init__(self, obj, as_varname=None):
        self.obj = template.Variable(obj)
        self.as_varname = as_varname

    def render(self, context):
        obj = self.obj.resolve(context)

        files = UploadedFile.objects.get_by_owner(obj)

        context[self.as_varname] = files
        return ''

def do_get_uploaded_files_by_owner(parser, token):
    try:
        parts = token.split_contents()

        obj, as_varname = parts[1], parts[3]
    except KeyError:
        raise template.TemplateSyntaxError(
                "You must inform the object, the 'as' operator and the variable name to ouput"
                )

    return UploadedFilesByOwnerNode(obj, as_varname)

register.tag('get_uploaded_files_by_owner', do_get_uploaded_files_by_owner)

