from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk
from .forms import ProdukForm


def produk_list(request):
    produk = Produk.objects.all()
    return render(request, 'produk/produk_list.html', {
        'produk': produk,
        'active_filter': 'all'
    })

def produk_bisa_dijual(request):
    produk = Produk.objects.filter(status__nama_status="bisa dijual")
    return render(request, 'produk/produk_list.html', {
        'produk': produk,
        'active_filter': 'bisa_dijual'
    })

def produk_tambah(request):
    if request.method == "POST":
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
    return render(request, 'produk/produk_form.html', {
        'form': form,
        'form_title': 'Tambah Data'
    })

def produk_edit(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == "POST":
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/produk_form.html', {
        'form': form,
        'form_title': 'Edit Data'
    })


def produk_hapus(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == "POST":  # konfirmasi hapus
        produk.delete()
        return redirect('produk_list')
    return render(request, 'produk/produk_konfirmasi_hapus.html', {'produk': produk})

