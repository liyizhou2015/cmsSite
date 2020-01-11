import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from photo.models import Photo
# Create your views here.


def photo_upload(request):
    return render(request, 'photo/photo_upload.html')


def photo_handle(request):
    f1 = request.FILES.get('pic')  # 从前端获取上传的图片   
    fname = '{}/booktest/{}'.format(settings.MEDIA_ROOT, f1.name)  # 图片的完整路径
    print(fname)
    with open(fname, 'wb') as pic:  # 文件操作
        for c in f1.chunks():  # 因为图片存储的方式是二进制流，用f1.chunks()获取图片的字节
            pic.write(c)
    pic1 = Photo()
    pic1.pic = 'booktest/%s' % f1.name
    pic1.save()
    return HttpResponse('OK')


def photo_show(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo/photo_show.html', context)
