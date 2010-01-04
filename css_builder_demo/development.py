from css_builder_demo.settings import *

DEBUG = True

INSTALLED_APPS += ('css_builder',)

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'django_css_builder_demo'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'
DATABASE_HOST = ''
DATABASE_PORT = ''

CSS_BUILDER_SOURCE = here(('media', 'internal',))
CSS_BUILDER_SPRITES = {
    'sprite_1': {
                'files':['opera.png', 'ff.png', 'safari.png'],
                'orientation': 'vertically'}
}
