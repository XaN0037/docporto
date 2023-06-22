from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.formats import patient_format_all, patient_format_one, file_format
from base.errors import *
from dashboard.models import Files
from dashboard.v1.files.serializer import FilesSerializer






class FileViews(GenericAPIView):
    serializer_class = FilesSerializer
    permission_classes = (AllowAny,)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()

        return Response(file_format(root))


    def get(self, requests, *args, **kwargs):
        if not requests.query_params.get('pk'):
            files = Files.objects.all()
            if not files:
                return Response(MESSAGE['NotData'])
            return Response({"data": [file_format(i) for i in files]})
        if requests.query_params.get('pk'):
            file = Files.objects.filter(pk=requests.query_params.get('pk')).first()
            if not file:
                return Response(MESSAGE['NotData'])
            return Response({"data": file_format(file)})

    def put(self, requests, *args, **kwargs):
        try:
            file = Files.objects.get(pk=requests.query_params.get('pk'))
            serializer = self.get_serializer(data=requests.query_params, instance=file, partial=True)
            serializer.is_valid(raise_exception=True)
            root = serializer.save()
            return Response(file_format(root))

        except:
            return Response(MESSAGE["PatientNotFound"])

    def delete(self, requests, *args, **kwargs):
        try:
            root = Files.objects.get(pk=requests.query_params.get('pk'))
            root.delete()
            return Response({"o\'chirildi": file_format(root)})
        except:
            return Response(MESSAGE["NotData"])
