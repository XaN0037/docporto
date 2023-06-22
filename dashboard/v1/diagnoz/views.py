from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.formats import patient_format_all, patient_format_one
from base.errors import *
from dashboard.models import Diagnoz
from dashboard.v1.diagnoz.serializer import DiagnozSerializer


class PatientViews(GenericAPIView):
    serializer_class = DiagnozSerializer
    permission_classes = (AllowAny,)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()

        return Response(patient_format_all(root))

    def get(self, requests, *args, **kwargs):
        if not requests.query_params.get('pk'):
            diagnoz = Diagnoz.objects.all()
            if not diagnoz:
                return Response(MESSAGE['NotData'])
            return Response({"data": [patient_format_all(i) for i in diagnoz]})
        if requests.query_params.get('pk'):
            patient = Diagnoz.objects.filter(pk=requests.query_params.get('pk')).first()
            if not patient:
                return Response(MESSAGE['NotData'])
            return Response({"data": patient_format_one(patient)})

    def put(self, requests, *args, **kwargs):
        patient = ''
        try:
            patient = Patient.objects.get(pk=requests.query_params.get('pk'))
            serializer = self.get_serializer(data=requests.query_params, instance=patient, partial=True)
            serializer.is_valid(raise_exception=True)
            root = serializer.save()
            return Response(patient_format_one(root))

        except:
            return Response(MESSAGE["PatientNotFound"])

    def delete(self, requests, *args, **kwargs):
        try:
            root = Patient.objects.get(pk=requests.query_params.get('pk'))
            root.delete()
            return Response(MESSAGE[f"Doctordelet"])
        except:
            return Response(MESSAGE["Doctordeleteerror"])
