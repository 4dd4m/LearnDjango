from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from tree.models import Genre

admin.site.register(
    Genre,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
