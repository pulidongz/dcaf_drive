from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from .models import *

admin.site.register(Dat, FileAdmin)
# admin.site.register(Tiff, FileAdmin)
# admin.site.register(Sbx, FileAdmin)
