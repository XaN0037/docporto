from django.core.paginator import Paginator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.formats import diagnoz_format_one, diagnoz_format_all
from base.errors import *
from dashboard.models import Diagnoz
from dashboard.v1.diagnoz.serializer import DiagnozSerializer
from src import settings


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
                pagination = Diagnoz.objects.all().order_by('-pk')
                paginator = Paginator(pagination, settings.PAGINATE_BY)
                page_number = requests.query_params.get("page", 1)
                return Response(diagnoz_format_all(x) for x in paginator.get_page(page_number))
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
