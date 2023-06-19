from django.core.paginator import Paginator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import New
from base.errors import MESSAGE
from base.formats import new_format_all, new_format
from src import settings


class NewViews(GenericAPIView):

    # def post(self, requests, *args, **kwargs):
    #     pass

    def get(self, requests, *args, **kwargs):
        if requests.query_params.get('pk'):
            try:
                return Response({"data": new_format_all(New.objects.filter(pk=requests.query_params.get('pk')).first(),
                                                        "uz" if not requests.query_params.get(
                                                            'lan') else requests.query_params.get('lan'))})
            except:
                return Response({MESSAGE['NewGetIdError']})
            
        try:
            return Response({"data": [
                new_format(i, "uz" if not requests.query_params.get('lan') else requests.query_params.get('lan')) for
                i in Paginator(New.objects.all().order_by('-pk'), settings.PAGINATE_BY).get_page(
                    requests.GET.get("page", 1))]})
        except:
            return Response({MESSAGE['NewGetError']})

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
