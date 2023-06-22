from rest_framework import serializers

from dashboard.models import Files


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

