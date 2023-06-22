from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.formats import diagnoz_format_one, diagnoz_format_all
from base.errors import *
from dashboard.models import Diagnoz
from dashboard.v1.diagnoz.serializer import DiagnozSerializer


class DiagnozViews(GenericAPIView):
    serializer_class = DiagnozSerializer
    permission_classes = (AllowAny,)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()

        return Response(diagnoz_format_one(root))

    def get(self, requests, *args, **kwargs):
        if requests.query_params.get('pk'):
            try:
                return Response(
                    {"data": diagnoz_format_one(Diagnoz.objects.filter(pk=requests.query_params.get('pk')).first())})
            except:
                return Response(MESSAGE['NotData'])
        if not requests.query_params.get('pk'):
            try:
                return Response({"data": [diagnoz_format_all(i) for i in Diagnoz.objects.all()]})
            except:
                return Response(MESSAGE['NotData'])

    def put(self, requests, *args, **kwargs):
        try:
            patient = Diagnoz.objects.get(pk=requests.query_params.get('pk'))
            serializer = self.get_serializer(data=requests.query_params, instance=patient, partial=True)
            serializer.is_valid(raise_exception=True)
            root = serializer.save()
            return Response(diagnoz_format_one(root))

        except:
            return Response(MESSAGE["PatientNotFound"])

    def delete(self, requests, *args, **kwargs):
        try:
            root = Diagnoz.objects.get(pk=requests.query_params.get('pk'))
            root.delete()
            return Response(MESSAGE[f"Doctordelet"])
        except:
            return Response(MESSAGE["Doctordeleteerror"])
