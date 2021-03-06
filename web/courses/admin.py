from django.contrib import admin
from .models import Course, ProblemSet, StudentEnrollment


class StudentEnrollmentInline(admin.StackedInline):
    model = StudentEnrollment


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'teachers',
        'students',
    )
    inlines = (
        StudentEnrollmentInline,
    )


class ProblemSetAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'title',
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'course',
    )
    ordering = (
        'course',
        '_order',
    )
    search_fields = (
        'title',
        'description',
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(ProblemSet, ProblemSetAdmin)
