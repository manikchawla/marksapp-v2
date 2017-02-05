from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Batch, Student, Teacher, Subject, Marks, BatchSubject, Coordinator

class BatchAdmin(ModelAdmin):
	list_display = ['name', 'semester', 'stream']

class StudentAdmin(ModelAdmin):
	list_display = ['batch', 'name', 'roll_no', 'phone']

class TeacherAdmin(ModelAdmin):
	list_display = ['name', 'phone']

class SubjectAdmin(ModelAdmin):
	list_display = ['id', 'name']

class BatchSubjectAdmin(ModelAdmin):
	list_display = ['teacher', 'batch', 'subject']

class MarksAdmin(ModelAdmin):
	list_display = ['student', 'subject', 'first_sessional', 
					'second_sessional', 'internal_assessment',
                    'total_internal_marks']

class CoordinatorAdmin(ModelAdmin):
    list_display = ['batch', 'teacher']

admin.site.site_header = 'Marksapp Administration'
admin.site.register(BatchSubject, BatchSubjectAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)