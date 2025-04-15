from django.contrib import admin
from common import models 

@admin.register(models.Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle",)
    search_fields = ("title", "subtitle",)


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")

@admin.register(models.Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("title", "content", )
    search_fields = ("title", "content",)

@admin.register(models.IntroImages)
class IntroImagesAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)

@admin.register(models.FDS)
class FDSAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title",)

@admin.register(models.KPT)
class KPTAdmin(admin.ModelAdmin):
    list_display = ("email",)
    search_fields = ("email",)
@admin.register(models.Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ("content",)
    search_fields = ("content",)

admin.site.register(models.Contacts)
