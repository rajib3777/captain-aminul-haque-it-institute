from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
        "plan",
        "is_dhaka16_voter",
        "dhaka16_area",
        "created_at",
    )

    list_filter = (
        "is_dhaka16_voter",
        "plan",
        "dhaka16_area",
    )

    search_fields = (
        "user__username",
        "phone",
        "dhaka16_area",
    )
