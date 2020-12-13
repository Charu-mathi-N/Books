from django.contrib import admin
from .models import Books
#from .models import Cart
# Register your models here.

admin.site.register(Books)

class BooksAdmin(admin.ModelAdmin):
    pass
