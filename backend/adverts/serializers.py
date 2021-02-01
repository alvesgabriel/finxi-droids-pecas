from backend.adverts.models import Address, Advert
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "zip_code",
            "number",
            "street",
            "district",
            "city",
            "uf",
        )


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = (
            "address",
            "description",
            "opened",
        )


class AdvertInfoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.first_name")
    email = serializers.EmailField(source="user.email")
    address = AddressSerializer(many=False)

    class Meta:
        model = Advert
        fields = (
            "id",
            "user",
            "email",
            "address",
            "description",
            "opened",
        )


class AdvertFinalizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("id",)

    def update(self, instance, validated_data):
        instance.opened = False
        instance.save()
        return instance
