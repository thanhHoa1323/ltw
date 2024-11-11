from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TrangChu, GioiThieu, LienHe, DichVu, SanPham, TinTuc

def home(request):
    gioi_thieu = GioiThieu.objects.all()
    dich_vu = DichVu.objects.all()
    san_pham = SanPham.objects.all()
    tin_tuc = TinTuc.objects.all()
    return render(request, 'home.html', {
        'gioi_thieu': gioi_thieu,
        'dich_vu': dich_vu,
        'san_pham': san_pham,
        'tin_tuc': tin_tuc,
    })

# View cho Giới thiệu
def about(request):
    gioi_thieu = GioiThieu.objects.all()
    return render(request, 'about.html', {'gioi_thieu': gioi_thieu})

# View cho Liên hệ
def contact(request):
    lien_he = LienHe.objects.all()
    return render(request, 'contact.html', {'lien_he': lien_he})

# View cho Dịch vụ
def services(request):
    dich_vu = DichVu.objects.all()
    return render(request, 'services.html', {'dich_vu': dich_vu})

# View cho Sản phẩm
def products(request):
    san_pham = SanPham.objects.all()
    return render(request, 'products.html', {'san_pham': san_pham})

# View cho Tin tức
def news(request):
    tin_tuc = TinTuc.objects.all()
    return render(request, 'news.html', {'tin_tuc': tin_tuc})


def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse("Cảm ơn bạn đã gửi liên hệ!")
    else:
        return redirect('contact')
# Create your views here.
