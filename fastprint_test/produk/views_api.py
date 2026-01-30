from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Produk
from .serializers import ProdukSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

    def destroy(self, request, *args, **kwargs):
        confirm = request.data.get("confirm", False)

        if not confirm:
            return Response(
                {"detail": "Konfirmasi diperlukan untuk menghapus data. Tambahkan 'confirm': true."},
                status=status.HTTP_400_BAD_REQUEST
            )

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Produk berhasil dihapus."}, status=status.HTTP_204_NO_CONTENT)
