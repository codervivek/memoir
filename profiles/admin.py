from django.contrib import admin
from .models import Department,Professor,Category,CategoryList


admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Category)
admin.site.register(CategoryList)
