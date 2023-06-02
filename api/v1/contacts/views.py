from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.models import Contact
from api.v1.contacts.serializer import ContactSerializer
from base.formats import contact_format
from base.errors import *


class ContactViews(GenericAPIView):
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)

    # def post(self, requests, *args, **kwargs):
    #     if Contact.objects.all():
    #         return Response(MESSAGE["Contactsadderror"])
    #     serializer = self.get_serializer(data=requests.data)
    #     serializer.is_valid(raise_exception=True)
    #     root = serializer.save()
    #
    #     return Response(contact_format(root))

    def get(self, requests,*args, **kwargs):
        data = requests.query_params
        contacts = Contact.objects.all().first()
        if not contacts:
            return Response(MESSAGE['NotData'])
        return Response({"data": contact_format(contacts,"uz" if not data.get('lan') else data.get('lan'))})

    # def put(self, requests, pk, *args, **kwargs):
    #     data = requests.data
    #     contact = ''
    #     try:
    #         contact = Contact.objects.get(pk=pk)
    #         serializer = self.get_serializer(data=data, instance=contact, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         root = serializer.save()
    #         return Response(contact_format(root))
    #
    #     except:
    #         return Response(MESSAGE["Contactsdeleteerror"])

    # def delete(self, requests, pk, *args, **kwargs):
    #     try:
    #         root = Contact.objects.get(pk=pk)
    #         result = MESSAGE["Contactsdelet"]
    #         root.delete()
    #         return Response(result)
    #     except:
    #         return Response(MESSAGE["Contactsdeleteerror"])
