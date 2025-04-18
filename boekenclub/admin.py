from django.contrib import admin

from boekenclub.models import Book, Profile, Read

admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Read)