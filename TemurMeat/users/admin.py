from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Customer

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'role')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_moderator():
            return qs.filter(role__in=['seller', 'customer'])
        elif request.user.is_seller():
            return qs.filter(role='customer')
        return qs

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'purchase_amount', 'is_confirmed')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_seller():
            return qs
        return qs

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer, CustomerAdmin)