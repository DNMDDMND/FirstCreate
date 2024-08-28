from django.db import models

from BookList.models import BookBasic,BookChapter

# Create your models here.
class User(models.Model):
    GENDER = (
        ('male',  u'男'),
        ('female', u'女'),
    )
    name = models.CharField(max_length=15,unique=True, verbose_name=u'用户名')
    password = models.CharField(max_length=200, verbose_name=u'密码')
    email = models.EmailField(unique=True, verbose_name=u'电子邮箱')
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True, default='', verbose_name=u'性别')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    isSuperUser = models.BooleanField(verbose_name=u'是否为超级用户',default = False)

    def __str__(self):
        return str(self.name)
    
#用户收藏的书籍
class UserBookCollection(models.Model):
    collected_at = models.DateTimeField(auto_now_add=True, verbose_name=u'收藏时间')
    notes = models.TextField(blank=True, verbose_name=u'备注')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'用户')
    book = models.ForeignKey(BookBasic, on_delete=models.CASCADE, verbose_name=u'书籍')
    class Meta:
        unique_together = (('user', 'book'),)
        index_together = (('user', 'book'),)

    def __str__(self):
        return f"{self.user.name} - {self.book.title}"
    
#记录点击书籍时用户的信息
class UserBookClick(models.Model):
    book = models.ForeignKey(BookBasic, on_delete=models.CASCADE, verbose_name='书籍')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    clicked_at = models.DateTimeField(auto_now_add=True, verbose_name='点击时间')

    def __str__(self):
        return f"{self.book.title} - {self.user.name}"

