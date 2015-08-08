from django import VERSION


if VERSION < (1, 7, 0):
    from semantic_ui.patch import patch_all
    patch_all()
