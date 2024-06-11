from .models import userlogin
from rest_framework import serializers

class userloginserializer(serializers.ModelSerializer):
    class Meta:
        model = userlogin
        fields = '__all__'

    # def __init__(self):
    #     self.get_