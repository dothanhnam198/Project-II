from django.contrib import admin
from database.models import *
# Register your models here.


class Teacher_Admin(admin.ModelAdmin):
    list_display = ['full_name']

    search_fields = ['full_name']


admin.site.register(Teacher, Teacher_Admin)


class Class_Admin(admin.ModelAdmin):
    list_display = ['grade', 'name']


admin.site.register(Class, Class_Admin)


class Subject_Admin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']


admin.site.register(Subject, Subject_Admin)


class Student_Admin(admin.ModelAdmin):
    list_display = ['full_name', 'class_id_id', 'date_of_birth']


admin.site.register(Student, Student_Admin)


class Score_Admin(admin.ModelAdmin):
    list_display = ['result', 'type', 'student_id', 'subject_id']


admin.site.register(Score, Score_Admin)


class Schedule_Admin(admin.ModelAdmin):
    list_display = ['semester', 'name']

    search_fields = ['semester', 'name']


admin.site.register(Schedule, Schedule_Admin)


class Lesson_Admin(admin.ModelAdmin):
    list_display = ['note', 'teacher_id', 'subject_id', 'class_id', 'schedule_id']


admin.site.register(Lesson, Lesson_Admin)