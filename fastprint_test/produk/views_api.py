from rest_framework import viewsets
from .models import Produk
from .serializers import ProdukSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
