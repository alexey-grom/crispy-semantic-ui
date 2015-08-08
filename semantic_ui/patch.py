from django.conf import settings
from crispy_forms import layout


def patch_all():
    if settings.CRISPY_TEMPLATE_PACK != 'semantic-ui':
        return

    layout.Submit.field_classes = 'ui primary button'
    layout.Button.field_classes = 'ui button'
    layout.Reset.field_classes = 'ui button'
    layout.Column.field_classes = 'column'
    layout.Field.field_classes = 'field'
