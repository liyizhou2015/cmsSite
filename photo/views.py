import os

from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from photo.models import Photo
# Create your views here.


def photo_upload(request):
    if request.user.is_anonymous:
        return redirect('/account/login')
    return render(request, 'photo/photo_upload.html')


def photo_handle(request):

    userFolder = "img/" + str(request.user.id) + "-" + \
        str(request.user.username)
    ffolder = '{}/{}'.format(settings.MEDIA_ROOT,
                             userFolder)
    if not os.path.exists(ffolder):
        os.makedirs(ffolder)

    f1 = request.FILES.get('pic')  # 从前端获取上传的图片
    fname = ffolder + "/" + f1.name  # 图片的完整路径
    # print(fname)

    with open(fname, 'wb') as pic:  # 文件操作
        for c in f1.chunks():  # 因为图片存储的方式是二进制流，用f1.chunks()获取图片的字节
            pic.write(c)

    pic1 = Photo()
    pic1.pic = '{}/{}'.format(userFolder, f1.name)
    pic1.author = request.user

    pic1.save()
    return HttpResponse('OK')


def photo_show(request):
    """
    相片列表 
    """
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo/photo_show.html', context)


def photo_detail(request):
    """
    显示相片详情
    """
    pass


def photo_delete_all(request):
    """
    删除所有相片
    """
    photos = Photo.objects.all()
    photos.delete()
    return HttpResponse("photos deleted")
