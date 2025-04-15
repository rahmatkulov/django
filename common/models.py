from django.db import models
from django.utils.translation import gettext_lazy as _

class Header(models.Model):
    title = models.CharField(_("title"), max_length=265)
    subtitle = models.CharField(_("subtitle"), max_length=265)
    video = models.FileField(_("video"), upload_to="videos/%Y/%m")

    class Meta:
        db_table = "header"
        verbose_name = _('header')
        verbose_name_plural = _("header")

    def __str__(self):
        return f"{self.title}" 


class Team(models.Model):
    name = models.CharField(_("name"), max_length=256)
    position = models.CharField(_("position"), max_length=256)
    image = models.ImageField(_("image"), upload_to="team/%Y/%m")

    class Meta:
        db_table = "team"
        verbose_name = _("team member")
        verbose_name_plural = _("team members")

    def __str__(self):
        return f"{self.name}" 

class Introduction(models.Model):
    title = models.CharField(_("title"), max_length=256)
    content = models.CharField(_("content"), max_length=256)
    class Meta:
        db_table = "intro"
        verbose_name = "title"
        verbose_name_plural = "title"

    def __str__(self):
        return f"{self.title}"


class IntroImages(models.Model):
    name = models.CharField(_("name"), max_length=256)
    image = models.ImageField(_("image"), upload_to="introimages/%Y/%m")
    class Meta:
        db_table = "image"
        verbose_name = "image"
        verbose_name_plural = "Introimages"

class FDS(models.Model):
    title = models.CharField(_("title"), max_length=256)
    content = models.CharField(_("content"), max_length=256)
    class Meta:
        db_table = "Content"
        verbose_name = "Title"
        verbose_name_plural = "Content"


class KPT(models.Model):
    phone_number = models.CharField(_("phone_number"), max_length=256)
    email = models.CharField(_("email"), max_length=256)
    location = models.CharField(_("location"), max_length=265)
    class Meta:
        db_table = "Contacts"
        verbose_name = "Contacts"
        verbose_name_plural = "Contacts"

class Socials(models.Model):
    content = models.CharField(_("content"), max_length=256)
    social = models.CharField(_("social"), max_length=256)
    class Meta:
        db_table = "Socials"
        verbose_name = "Social"
        verbose_name_plural = "Social"




class Contacts(models.Model):
    name = models.CharField(_("name"), max_length=256)
    email = models.CharField(_("email"), max_length=256)
    subject = models.CharField(_("subject"), max_length=256)
    message = models.CharField(_("message"), max_length=256)
    class Meta:
        db_table = _("contact",)
        verbose_name = _("contact",)
        verbose_name_plural = _("contacts", )

    def __str__(self):
        return f"{self.name}"

