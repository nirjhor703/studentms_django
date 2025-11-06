from django.contrib import admin
from .models import Student, Teacher, Subject, ClassModel

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(ClassModel)

