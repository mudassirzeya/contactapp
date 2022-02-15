from rest_framework.serializers import ModelSerializer
from .models import Contact
# from rest_framework.authtoken.models import Token


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
