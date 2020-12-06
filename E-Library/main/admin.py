from django.contrib import admin
from .models import Books
#from .models import Cart
# Register your models here.

admin.site.register(Books)

#admin.site.register(Cart)

#admin.site.register(User)
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    pass

class CartItemAdmin(admin.ModelAdmin):
    pass
