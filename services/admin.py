from django.contrib import admin
from django.utils.html import format_html   # <-- missing import
from .models import Service,Mechanic,Profile


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview", "description", "price", "duration", "rating")

    def image_preview(self, obj):
        if obj.image:   # make sure Service model has an ImageField called "image"
            return format_html(
                '<img src="{}" style="height:50px;width:50px;object-fit:cover;" />',
                obj.image.url
            )
        return "-"
    
    image_preview.short_description = "Image"   # <-- this line should be outside the function
@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "rating", "vehicle_number", "eta_minutes", "photo_preview")
    search_fields = ("name", "phone", "vehicle_number")

    def photo_preview(self, obj):
        if obj.photo:
            return f"<img src='{obj.photo.url}' width='50' height='50' style='border-radius:50%;' />"
        return "No Image"
    photo_preview.allow_tags = True
    photo_preview.short_description = "Photo"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "profile_image")
    search_fields = ("user__username", "user__email", "phone")