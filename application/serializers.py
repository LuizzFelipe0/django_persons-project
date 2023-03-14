from rest_framework import serializers
from .models import Person

class personSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , use_url=True)
    
    class Meta:
        model = Person
        fields = '__all__'