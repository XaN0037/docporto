from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.formats import retsep_format_one, retsep_format_all
from base.errors import *
from dashboard.models import Retsep
from dashboard.v1.retseps.serializer import RetsepSerializer


class RetsepViews(GenericAPIView):
    serializer_class = RetsepSerializer
    permission_classes = (AllowAny,)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()

        return Response(retsep_format_one(root))

    def get(self, requests, *args, **kwargs):
        if not requests.query_params('pk'):
            retseps = Retsep.objects.all()
            if not retseps:
                return Response(MESSAGE['NotData'])
            return Response({"data": [retsep_format_all(i) for i in retseps]})
        if requests.query_params.get('pk'):
            patient = Retsep.objects.filter(pk=requests.query_params.get('pk')).first()
            if not patient:
                return Response(MESSAGE['NotData'])
            return Response({"data": retsep_format_one(patient)})

    def put(self, requests, *args, **kwargs):
        patient = ''
        try:
            retsep = Retsep.objects.get(pk=requests.query_params.get('pk'))
            print(retsep_format_all(patient))
            serializer = self.get_serializer(data=requests.query_params, instance=retsep, partial=True)
            serializer.is_valid(raise_exception=True)
            root = serializer.save()
            return Response(retsep_format_one(root))

        except:
            return Response(MESSAGE["DoctorNotFound"])

    def delete(self, requests, *args, **kwargs):
        try:
            root = Retsep.objects.get(pk=requests.query_params.get('pk'))
            root.delete()
            return Response(MESSAGE[f"Doctordelet"])
        except:
            return Response(MESSAGE["Doctordeleteerror"])