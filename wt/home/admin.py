from django.contrib import admin
from .models import address , contact_form , WorkwithUS , blog_comment , blogs , services_contact , it_services , con_services , about_us, slider, brand_logo , social_media
from django.utils.html import format_html




# Register your models here.

class addressAdmin(admin.ModelAdmin):
    list_display = ('created_at','phone','email','adr','office_time','office_loacation',)
    ordering=('created_at',)

class contact_formAdmin(admin.ModelAdmin):
    list_display = ('created_at','name','phone','email','subject','msg',)
    ordering=('created_at',)

class WorkwithUSAdmin(admin.ModelAdmin):
    list_display = ('created_at','name','phone','email','subject','msg',)
    ordering=('created_at',)

class blogsAdmin(admin.ModelAdmin):
    list_display = ('image_preview','created_At','title','content','active',)
    ordering=('created_At',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="border-radius:10px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"

class blog_commentAdmin(admin.ModelAdmin):
    list_display = ('created_at','blog_id','first_name','last_name','first_name','email','msg',)
    ordering=('created_at',)


class it_servicesAdmin(admin.ModelAdmin):
    list_display = ('created_at','image_preview','title','active',)
    ordering=('created_at',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="border-radius:10px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"



class con_servicesAdmin(admin.ModelAdmin):
    list_display = ('created_at','image_preview','title','active',)
    ordering=('created_at',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="border-radius:10px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"


class services_contactAdmin(admin.ModelAdmin):
    list_display = ('created_at','name','phone','email','subject','msg',)
    ordering=('created_at',)

class about_usAdmin(admin.ModelAdmin):
    list_display = ('created_at','image_preview' ,'title','content','active',)
    ordering=('created_at',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="border-radius:10px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"


class brand_logoAdmin(admin.ModelAdmin):
    list_display = ('created_at','image_preview','title','active',)
    ordering=('created_at',)
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="border-radius:10px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"


class sliderAdmin(admin.ModelAdmin):
    list_display = ('created_at','image_preview','title','content','active',)
    ordering=('created_at',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{ obj.image.url}" width="100" height="100" style="border-radius:10px;" />')
        return "No Image"

    image_preview.short_description = "Image Preview"




admin.site.register(address, addressAdmin)
admin.site.register(contact_form, contact_formAdmin)
admin.site.register(WorkwithUS, WorkwithUSAdmin)
admin.site.register(blogs , blogsAdmin)
admin.site.register(blog_comment, blog_commentAdmin)
admin.site.register(it_services,it_servicesAdmin)
admin.site.register(con_services, con_servicesAdmin)
admin.site.register(services_contact, services_contactAdmin)
admin.site.register(about_us, about_usAdmin)
admin.site.register(slider, sliderAdmin)
admin.site.register(brand_logo , brand_logoAdmin)
admin.site.register(social_media)


