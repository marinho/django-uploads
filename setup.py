# django-uploads setup
# First version of this file done by Guilherme Semente

# Downloads setuptools if not find it before try to import
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
from uploads import get_version

setup(
    name = 'django-uploads',
    version = get_version(),
    description = 'A Django pluggable application to attach files to objects',
    long_description = 'django-uploads is a pluggable application for Django projects that allows users attach files to other objects.',
    author = 'Marinho Brandao',
    author_email = 'marinho@gmail.com',
    url = 'http://github.com/marinho/django-uploads/',
    license = 'GNU Lesser General Public License (LGPL)',
    packages = ['uploads', 'uploads.templatetags'],
)
