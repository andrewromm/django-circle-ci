from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _


class Author(models.Model):
    first_name = models.CharField(_("Имя"), max_length=50, blank=False, null=False)
    last_name = models.CharField(_("Фамилия"), max_length=50, blank=False, null=False)
    patronymic = models.CharField(_("Отчество"), max_length=50, blank=True)

    class Meta:
        verbose_name="автор"
        verbose_name_plural="авторы"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Book(models.Model):
    name = models.CharField(_("Название книги"), max_length=100, blank=False, null=False)
    description = models.TextField(_("Описание книги"))
    author = models.ForeignKey(Author, verbose_name=_("автор"), on_delete=models.CASCADE)

    class Meta:
        verbose_name="книга"
        verbose_name_plural="книги"

    def __str__(self):
        return f"{self.name}"
