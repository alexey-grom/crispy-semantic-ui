from django.apps import AppConfig


class SemanticUIConfig(AppConfig):
    name = 'semantic_ui'
    verbose_name = 'semantic_ui'

    def ready(self):
        super(SemanticUIConfig, self).ready()

        from semantic_ui import patch
        patch.patch_all()
