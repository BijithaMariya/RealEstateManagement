from django.contrib import admin
from . models import studentInfo,adminUser,tenantUser

# Register your models here.
admin.site.register(studentInfo)
admin.site.register(adminUser)
admin.site.register(tenantUser)
