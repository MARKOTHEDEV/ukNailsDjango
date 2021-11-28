from django.contrib import admin

from .models import (
    User,
    Service,
    ServiceCategory,
    ServiceCategoryAddOns,
    Bookings,Testimonial

)

class ServiceCategoryAddOnsInline__InServiceCategory(admin.TabularInline):
    model =ServiceCategoryAddOns
    extra=1

class ServiceCategoryTabulaAdminDesign(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['name','amount','service','image']})]
    inlines=[ServiceCategoryAddOnsInline__InServiceCategory]

# admin.site.register(Testimonial)

admin.site.register(
    User

)
admin.site.register(

        Service
)
admin.site.register(ServiceCategory ,ServiceCategoryTabulaAdminDesign)
# admin.site.register(ServiceCategoryAddOns,ServiceCategoryAddOnsInline__InServiceCategory )
admin.site.register(

        Bookings
)







