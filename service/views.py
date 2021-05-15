from django.db.migrations import serializer
from django.http import Http404
from rest_flex_fields.views import FlexFieldsModelViewSet
from rest_framework import viewsets, status, response, decorators, parsers, request
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from service.models import UrunFiyat, UrunOzellikleri, IlceModel, SehirModel, KategoriModel, AltKategoriModel, \
    UrunModel, UrunResimler, AdresModel
from service.serializers import UrunFiyatSerializer, UrunOzellikleriSerializer, IlceSerializer, SehirSerializer, \
    KategoriSerializer, AltKategoriSerializer, UrunSerializer, UrunResimlerSerializer, AdresSerializer, \
    UrunDetailSerializer


class IlceViewSet(viewsets.ModelViewSet):
    queryset = IlceModel.objects.all()
    serializer_class = IlceSerializer


class SehirViewSet(viewsets.ModelViewSet):
    queryset = SehirModel.objects.all()
    serializer_class = SehirSerializer

class AdresViewSet(viewsets.ModelViewSet):
    queryset = AdresModel.objects.all()
    serializer_class = AdresSerializer



class KategoriViewSet(viewsets.ModelViewSet):
    queryset = KategoriModel.objects.all()
    serializer_class = KategoriSerializer


class AltKategoriViewSet(FlexFieldsModelViewSet):
    queryset = AltKategoriModel.objects.all()
    serializer_class = AltKategoriSerializer


class UrunViewSet(viewsets.ModelViewSet):
    queryset = UrunModel.objects.all()
    serializer_class = UrunSerializer
    lookup_field = "slug"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["adi"]

class UrunDetailSet(viewsets.ModelViewSet):
    queryset = UrunResimler.objects.all()
    serializer_class = UrunDetailSerializer

class UrunResimlerViewSet(viewsets.ModelViewSet):
    queryset = UrunResimler.objects.all()
    serializer_class = UrunResimlerSerializer

    @decorators.action(
        detail=True,
        methods=['POST'],
        parser_classes=[parsers.MultiPartParser],
    )

    def resim_ekle(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)


class UrunOzellikleriViewSet(viewsets.ModelViewSet):
    queryset = UrunOzellikleri.objects.all()
    serializer_class = UrunOzellikleriSerializer

class UrunFiyatViewSet(viewsets.ModelViewSet):
    queryset = UrunFiyat.objects.all()
    serializer_class = UrunFiyatSerializer


class Files_APIView(APIView):
    # parser_class = (FileUploadParser, )
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    # permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None, *args, **kwargs):
        file = UrunResimler.objects.all()
        serializer = UrunResimlerSerializer(file, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UrunResimlerSerializer(data=request.data)
        resim_list = request.FILES.getlist('urunresim')

        if serializer.is_valid():
            for item in resim_list:
                f = UrunResimler.objects.create(urun=request.data['urun'], urunresim=item,sliderresim=request.data['sliderresim'],)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    Post implementation #3
        - With error: AttributeError
        - Save multiple files
        - Use FileListSerializer
"""


# def post(self, request, format=None):
#     serializer = FileListSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Files_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return UrunResimler.objects.get(pk=pk)
        except UrunResimler.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = UrunResimler(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = UrunResimler(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)