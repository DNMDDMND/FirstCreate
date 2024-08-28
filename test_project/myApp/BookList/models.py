from django.db import models

# Create your models here.

#书籍类型
bookType = [
        ('Xuanhuan', '玄幻'),
        ('Qihuan', '奇幻'),
        ('Wuxia', '武侠'),
        ('Xianxia', '仙侠'),
        ('Dushi', '都市'),
        ('Xianshi', '现实'),
        ('Junshi', '军事'),
        ('Lishi', '历史'),
        ('Youxi', '游戏'),
        ('Tiyu', '体育'),
        ('Kehuan', '科幻'),
        ('Wuxian', '诸天无限'),
        ('Xuanyi', '悬疑灵异'),
        ('Qing', '轻小说'),
    ]

#书籍基本信息
class BookBasic(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'标题')
    author = models.CharField(max_length=200, verbose_name=u'作者')
    type = models.CharField(max_length=20,choices=bookType,verbose_name=u'类型')
    description = models.TextField(verbose_name=u'简介')
    cover_image_url = models.CharField(max_length=500, verbose_name=u'封面路径')
    content_url = models.CharField(max_length=500, verbose_name=u'内容路径')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    click_count = models.IntegerField(default=0, verbose_name='点击量')
    
    def __str__(self):
        return self.title
    
#书籍目录和章节内容
class BookChapter(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'标题')
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    content = models.TextField(verbose_name=u'章节内容')
    book = models.ForeignKey(BookBasic, on_delete=models.CASCADE, verbose_name=u'书籍')
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    