from rest_framework import serializers
from home.models import *

class todoserializers(serializers.ModelSerializer):
    class Meta:
        model=todo 
        fields='__all__'
        
        