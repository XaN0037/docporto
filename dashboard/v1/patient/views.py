from django.conf import settings
from django.core.paginator import Paginator
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
                return Response(MESSAGE['NotData'], status=404)
        if not requests.query_params.get('pk'):
            try:
                pagination = Patient.objects.all().order_by('-pk')
                paginator = Paginator(pagination, settings.PAGINATE_BY)
                page_number = requests.query_params.get("page", 1)
                return Response(patient_format_all(x) for x in paginator.get_page(page_number))
            except:
                return Response(MESSAGE['NotData'], status=404)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        try:
            patient = Patient.objects.get(pk=pk)
        except:
            return Response(MESSAGE['NotData'], status=404)

        patient.name = data.get('name', patient.name)
        patient.first_name = data.get('first_name', patient.first_name)
        patient.father_name = data.get('father_name', patient.father_name)
        patient.age = data.get('age', patient.age)
        patient.phone = data.get('phone', patient.phone)
        patient.comment = data.get('comment', patient.comment)

        patient.save()

        return Response(patient_format_one(patient))

    def delete(self, requests, *args, **kwargs):
        try:
            root = Patient.objects.get(pk=requests.query_params.get('pk'))
            root.delete()
            return Response(MESSAGE[f"Doctordelet"])
        except:
            return Response(MESSAGE["Doctordeleteerror"], status=404)
