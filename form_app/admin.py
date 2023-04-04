from django.contrib import admin
from .models import Registeration_form, Person
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")


admin.site.register(Registeration_form)
