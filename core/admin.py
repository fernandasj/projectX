from django.contrib import admin
from .models import Teacher, Student

# =====================
# TeacherAdmin
# =====================
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('idTeacher', 'name', 'email', 'dateOfBirth', 'gender', 'user')

admin.site.register(Teacher, TeacherAdmin)


# ====================
# StudentAdmin
# ====================
class StudentAdmin(admin.ModelAdmin):
    list_display = ('idStudent', 'name', 'email', 'dateOfBirth', 'gender',
        'course', 'user')

admin.site.register(Student, StudentAdmin)
