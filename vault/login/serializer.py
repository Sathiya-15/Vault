from .models import userlogin
from rest_framework import serializers

class userloginserializer(serializers.ModelSerializer):
    class Meta:
        model = userlogin
        fields = '__all__'