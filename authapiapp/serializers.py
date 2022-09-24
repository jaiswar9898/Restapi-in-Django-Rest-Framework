from rest_framework import serializers

from authapiapp.models import user


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
    

