from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

from alinxin_app.settings import MEDIA_URL


class Test(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名", default="")
    photo = models.CharField(max_length=20, verbose_name="员工id", default="")
    content = RichTextField(max_length=200, verbose_name="内容", default="")
    image = models.ImageField(upload_to='image', verbose_name='图片', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True)
    video = models.FileField(upload_to="video", verbose_name='视频', null=True, blank=True)

    # 后台控制台显示图片
    def admin_sample(self):
        return mark_safe('<img src="%s%s" height="50" width="50" />' % (MEDIA_URL, self.image,))

    admin_sample.short_description = '图片'
    admin_sample.allow_tags = True

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '个人详情'
        verbose_name_plural = '个人详情'
