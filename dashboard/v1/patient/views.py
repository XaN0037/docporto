from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.formats import patient_format_all, patient_format_one
from base.errors import *
from dashboard.models import Patient
from dashboard.v1.patient.serializer import PatientSerializer


class PatientViews(GenericAPIView):
    serializer_class = PatientSerializer
    permission_classes = (AllowAny,)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()

        return Response(patient_format_all(root))

    def get(self, requests, *args, **kwargs):
        if requests.query_params.get('pk'):
            try:
                return Response(
                    {"data": patient_format_one(Patient.objects.filter(pk=requests.query_params.get('pk')).first())})
            except:
                return Response(MESSAGE['NotData'])
        if not requests.query_params.get('pk'):
            try:
                return Response({"data": [patient_format_all(i) for i in Patient.objects.all()]})
            except:
                return Response(MESSAGE['NotData'])

    def put(self, requests, *args, **kwargs):
        try:
            patient = Patient.objects.get(pk=requests.query_params.get('pk'))
            serializer = self.get_serializer(data=requests.query_params, instance=patient, partial=True)
            serializer.is_valid(raise_exception=True)
            root = serializer.save()
            return Response(patient_format_one(root))
        except:
            return Response(MESSAGE["Doctordeleteerror"])

    def delete(self, requests, *args, **kwargs):
        try:
            root = Patient.objects.get(pk=requests.query_params.get('pk'))
            root.delete()
            return Response(MESSAGE[f"Doctordelet"])
        except:
            return Response(MESSAGE["Doctordeleteerror"])
