from django.db import models
class TrangChu(models.Model):
    ten = models.CharField(max_length=200)
    noi_dung = models.TextField()
    hinh_anh = models.ImageField(upload_to='images/trang_chu/')
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten
class GioiThieu(models.Model):
    ten = models.CharField(max_length=200)
    noi_dung = models.TextField()
    hinh_anh = models.ImageField(upload_to='images/gioi_thieu/')
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten
class LienHe(models.Model):
    ten = models.CharField(max_length=200)
    dia_chi = models.CharField(max_length=500)
    so_dien_thoai = models.CharField(max_length=20)
    email = models.EmailField()
    noi_dung = models.TextField()
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten
class DichVu(models.Model):
    ten = models.CharField(max_length=200)
    mo_ta = models.TextField()
    hinh_anh = models.ImageField(upload_to='images/dich_vu/')
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten
class SanPham(models.Model):
    ten = models.CharField(max_length=200)
    mo_ta = models.TextField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    hinh_anh = models.ImageField(upload_to='images/san_pham/')
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten
class TinTuc(models.Model):
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    hinh_anh = models.ImageField(upload_to='images/tin_tuc/')
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tieu_de
# Create your models here.
