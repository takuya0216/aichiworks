from django.contrib import admin

from .models import Process,Employee,Department,Position,Status,Message
# Register your models here.
admin.site.register(Process)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Status)
admin.site.register(Message)
