from rest_framework import serializers

from dashboard.models import Diagnoz


class DiagnozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnoz
        fields = '__all__'


