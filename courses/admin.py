from django.contrib import admin

from courses.db import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'deleted', 'creation_date']
    pass


admin.site.register(Course, CourseAdmin)
