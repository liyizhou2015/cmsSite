from datetime import datetime

from django.db import models
from django.conf import settings

# Create your models here.


class Photo(models.Model):
    # caption = models.CharField(max_length=250, blank=True, null=True)
    # views = models.PositiveIntegerField(default=0)
    # file_md5 = models.CharField(max_length=128)
    # file_type = models.CharField(max_length=32)
    # file_size = models.IntegerField()
    # created_at = models.DateTimeField(default=datetime.now)
    pic = models.ImageField(upload_to='booktest')

    # 我们还定义了通过文件md5值获取模型对象的类方法
    # @classmethod
    # def getImageByMd5(cls, md5):
    #     try:
    #         return UploadImage.objects.filter(file_md5=md5).first()
    #     except Exception as e:
    #         return None

    # # 获取本图片的url，我们可以通过这个url在浏览器访问到这个图片
    # # 其中settings.WEB_HOST_NAME 是常量配置，指你的服务器的域名
    # # settings.WEB_IMAGE_SERVER_PATH 也是常量配置，指你的静态图片资源访问路径
    # # 这些配置项我在Django项目的settings.py文件中进行配置
    # def getImageUrl(self):
    #     filename = self.file_md5 + "." + self.file_type
    #     url = settings.WEB_HOST_NAME + settings.WEB_IMAGE_SERVER_PATH + filename
    #     return url

    # # 获取本图片在本地的位置，即你的文件系统的路径，图片会保存在这个路径下
    # def getImagePath(self):
    #     filename = self.file_md5 + "." + self.file_type
    #     path = settings.IMAGE_SAVING_PATH + filename
    #     return path

    # def __str__(self):
    #     s = "filename:" + str(self.filename) + " - " + "filetype:" + str(self.file_type) \
    #         + " - " + "filesize:" + \
    #         str(self.file_size) + " - " + "filemd5:" + str(self.file_md5)
    #     return s
