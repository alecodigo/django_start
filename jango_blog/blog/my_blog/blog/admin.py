from django.contrib import admin
from .models import Post
#Esto hace tu modelo visible desde el administrador de django.

admin.site.register(Post)
