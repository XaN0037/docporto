from rest_framework import serializers

from dashboard.models import Retsep


class RetsepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retsep
        fields = '__all__'


