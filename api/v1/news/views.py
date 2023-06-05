from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import New
from base.errors import MESSAGE
from base.formats import new_format_all, new_format


#
# img = models.ImageField("Yangilikga oid rasm")
# title = models.CharField('Yangilikning Sarlavha', max_length=512)
# short_desc = models.TextField("Yangilikning Qisqa ma'lumoti")
# desc = models.TextField("Yangilikning To'liq ma'lumoti")
# date = models.DateField("Yangilikni saytga joylash vaqti", auto_now_add=True)


class NewViews(GenericAPIView):

    # def post(self, requests, *args, **kwargs):
    #     pass

    def get(self, requests, *args, **kwargs):
        data = requests.query_params
        if not requests.query_params.get('pk'):
            news = ''
            try:
                news = [new_format(i, "uz" if not requests.query_params.get('lan') else requests.query_params.get('lan')) for i in New.objects.all()]
            except:
                news = MESSAGE['NewGetError']
            return Response({"data": news})

        if requests.query_params.get('pk'):
            try:
                new = new_format_all(New.objects.filter(pk=requests.query_params.get('pk')).first(), "uz" if not requests.query_params.get('lan') else requests.query_params.get('lan'))
            except:
                new = MESSAGE['NewGetIdError']
            return Response({"data": new})

    # def put(self,requests, pk=None, *args, **kwargs):
    #     data = requests.data
    #     new = ''
    #     try:
    #         new = New.objects.get(pk=pk)
    #         print(new)
    #         serializer = self.get_serializer(data=data, instance=new, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         root = serializer.save()
    #         return Response(new_format(root))
    #
    #     except:
    #         return Response(MESSAGE["NewPutError"])
