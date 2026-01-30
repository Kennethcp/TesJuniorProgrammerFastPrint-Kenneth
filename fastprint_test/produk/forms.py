from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['id_produk', 'nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'id_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'kategori': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_id_produk(self):
        id_produk = self.cleaned_data.get('id_produk')

        # pastikan angka positif
        try:
            id_produk = int(id_produk)
        except (ValueError, TypeError):
            raise forms.ValidationError("ID produk harus berupa angka.")

        if id_produk <= 0:
            raise forms.ValidationError("ID produk tidak boleh negatif atau nol.")

        # cek duplikat hanya jika tambah atau edit ke produk lain
        qs = Produk.objects.filter(id_produk=id_produk)
        if self.instance.pk:  # sedang edit
            qs = qs.exclude(pk=self.instance.pk)  # abaikan produk yang sedang diedit

        if qs.exists():
            raise forms.ValidationError("ID produk sudah ada, gunakan ID lain.")

        return id_produk

    def clean_nama_produk(self):
        nama = self.cleaned_data.get('nama_produk')
        if not nama:
            raise forms.ValidationError("Nama produk harus diisi")
        return nama

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga is None or harga <= 0:
            raise forms.ValidationError("Harga harus berupa angka positif")
        return harga
