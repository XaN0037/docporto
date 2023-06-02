from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Doctor
from api.v1.doctors.serializer import DoctorSerializer
from base.formats import doctor_format
from base.errors import *


class DoctorViews(GenericAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (AllowAny,)

    # def post(self, requests, *args, **kwargs):
    #     serializer = self.get_serializer(data=requests.data)
    #     serializer.is_valid(raise_exception=True)
    #     root = serializer.save()
    #
    #     return Response(doctor_format(root))

    def get(self, requests, *args, **kwargs):
        data = requests.query_params
        doctors = Doctor.objects.all()

        if not doctors:
            return Response(MESSAGE['NotData'])
        return Response({"data": [doctor_format(i, 'uz' if not data.get('lan') else data.get('lan')) for i in doctors]})
    #
    # def put(self, requests, *args, **kwargs):
    #     data = requests.query_params
    #     doctor = ''
    #     try:
    #         doctor = Doctor.objects.get(pk=requests.query_params('pk'))
    #         serializer = self.get_serializer(data=data, instance=doctor, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         root = serializer.save()
    #         return Response(doctor_format(root))
    #
    #     except:
    #         return Response(MESSAGE["DoctorNotFound"])
    #
    # def delete(self, requests, *args, **kwargs):
    #     try:
    #         root = Doctor.objects.get(pk=requests.query_params('pk'))
    #         root.delete()
    #         return Response(MESSAGE[f"Doctordelet"])
    #     except:
    #         return Response(MESSAGE["Doctordeleteerror"])
