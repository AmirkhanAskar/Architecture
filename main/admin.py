from django.contrib import admin
from .models import MyBlogs, Author, Comment, Interiors, Exteriors, InteriorImage, ExteriorImage, Kitchens, KitchenImage, PrivateHouses, PrivateHouseImage

admin.site.register(MyBlogs)

admin.site.register(Author)

admin.site.register(Comment)

class InteriorImageInline(admin.TabularInline):
    model = InteriorImage
    extra = 3  # Количество дополнительных форм для загрузки изображений

class InteriorsAdmin(admin.ModelAdmin):
    inlines = [InteriorImageInline]

admin.site.register(Interiors, InteriorsAdmin)

class ExteriorImageInline(admin.TabularInline):
    model = ExteriorImage
    extra = 3  # Количество дополнительных форм для загрузки изображений

class ExteriorsAdmin(admin.ModelAdmin):
    inlines = [ExteriorImageInline]

admin.site.register(Exteriors, ExteriorsAdmin)


class KitchenImageInline(admin.TabularInline):
    model = KitchenImage
    extra = 3  # Количество дополнительных форм для загрузки изображений

class KitchensAdmin(admin.ModelAdmin):
    inlines = [KitchenImageInline]

admin.site.register(Kitchens, KitchensAdmin)



class PrivateHousesImageInline(admin.TabularInline):
    model = PrivateHouseImage
    extra = 3  # Количество дополнительных форм для загрузки изображений

class PrivateHousesAdmin(admin.ModelAdmin):
    inlines = [PrivateHousesImageInline]

admin.site.register(PrivateHouses, PrivateHousesAdmin)
