from backend.adverts import models
from django.contrib import admin
from django.utils.html import format_html


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "zip_code",
        "street",
        "district",
        "city",
        "uf",
        "number",
    )


@admin.register(models.Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "description",
        "address",
        "opened_img",
    )

    def opened_img(self, obj):
        img = {
            False: "/finxi-droids-pecas/static/assets/baseline-highlight_off.svg",
            True: "/finxi-droids-pecas/static/assets/baseline-check_circle_outline.svg",
        }
        return format_html(f'<img src="{img[obj.opened]}" width="15" height="15">')
