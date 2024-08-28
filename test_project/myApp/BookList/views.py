from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count,Sum

from BookList.models import bookType,BookBasic,BookChapter
from UserInfo.models import User,UserBookClick
import json,os,uuid
import re

BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AVATAR_ROOT = os.path.join(BASE_DIR, 'template/static/bookCover') # 书籍封面保存路径
CONTENT_ROOT = os.path.join(BASE_DIR, 'static/bookContent') # 书籍内容保存路径

covername_pattern = r'bookCover/(.*)'

# Create your views here.
def getBookType(request):
    return JsonResponse({'bookType':bookType})

def avatarUpload(request):
    response = {}
    # 获取前端发来的的file对象
    file = request.FILES.get('file')
    try:
        # 使用uuid生成唯一标识符
        uid = uuid.uuid4()
        filename = f'{uid}-{file.name}'
        
        # 构造图片保存路径 路径为<USER_AVATAR_ROOT + 文件名>
        # USER_AVATAR_ROOT刚刚在settings.py中规定过，需要导入进来
        file_path = os.path.join(AVATAR_ROOT, filename)
        # 保存图片
        with open(file_path, 'wb') as f:
            f.write(file.read())
        response['file'] = filename # 返回新的文件名
        response['code'] = 0
        response['msg'] = "图片上传成功！"
    except Exception as e:
        print('图片上传失败！原因为',e)
        response['file'] = ''
        response['code'] = 1
        response['msg'] = f"图片上传失败！原因为{e}"
    return JsonResponse(response)

def contentupload(request):
    response = {}
    # 获取前端发来的的file对象
    file = request.FILES.get('file')
    try:
        file_path = os.path.join(CONTENT_ROOT, file.name)
        # 保存书籍内容
        with open(file_path, 'wb') as f:
            f.write(file.read())
        response['filePath'] = file_path # 返回书籍正文路径
        response['code'] = 0
        response['msg'] = "书籍内容上传成功！"
    except Exception as e:
        print('书籍内容上传失败！原因为',e)
        response['file'] = ''
        response['code'] = 1
        response['msg'] = f"书籍内容上传失败！原因为{e}"
    return JsonResponse(response)

def submitBookList(request):
    response = {}
    try:
        #获取前端传来的bookList的数据
        bookBasicData = json.loads(request.POST.get('bookList'))
        
        # 检查是否有重复的标题和作者
        existing_books = BookBasic.objects.filter(title=bookBasicData['title'], author=bookBasicData['author'])
        if existing_books.exists():
            response['code'] = 1
            response['msg'] = "书籍提交失败！该书籍已存在！"
            return JsonResponse(response)
        
        #将bookList保存至BookBasic表
        bookBasicOne = BookBasic()
        bookBasicOne.title = bookBasicData['title']
        bookBasicOne.author = bookBasicData['author']
        bookBasicOne.type = bookBasicData['type']
        bookBasicOne.description = bookBasicData['description']
        bookBasicOne.cover_image_url = bookBasicData['cover_image_url']
        bookBasicOne.content_url = bookBasicData['content_url']
        bookBasicOne.save()
        
        #获取每一章的标题和内容
        with open(bookBasicData['content_url'],'r') as f:
            book_content = f.read()
        
        chapter_content_pattern = re.compile(r'-+\n(.*?)\n-', flags=re.DOTALL) # 匹配每一章节的内容，包括标题
        chapter_content = re.findall(chapter_content_pattern,book_content)
        
        for chapter_num,chapter_one in enumerate(chapter_content):
            chapter_one = chapter_one.strip('\n')
            chapter_title = chapter_one.split('\n')[0] #获取当前章节标题
            chapter_content_one = '\n'.join(chapter_one.split('\n')[1:]) #获取当前正文内容
            
            if chapter_content_one:
                # 创建 BookChapter 记录
                chapterOne = BookChapter(title=chapter_title, order=int(chapter_num),book=bookBasicOne,content=chapter_content_one)
                chapterOne.save()
            
        response['code'] = 0
        response['msg'] = "书籍提交成功！"
    except Exception as e:
        response['code'] = 1
        response['msg'] = f"书籍提交失败！原因为{e}"
    

    return JsonResponse(response)

def getBookCategory(request):
    response = {}
    try:
        book_type_counts = {
            'Xuanhuan':0,
            'Qihuan':0,
            'Wuxia':0,
            'Xianxia':0,
            'Dushi':0,
            'Xianshi':0,
            'Junshi':0,
            'Lishi':0,
            'Youxi':0,
            'Tiyu':0,
            'Kehuan':0,
            'Wuxian':0,
            'Xuanyi':0,
            'Qing':0
        }
        type_counts = BookBasic.objects.values('type').annotate(count=Count('type'))
        print('type_counts: ',type_counts)
        for item in type_counts:
            book_type_counts[item['type']] = item['count']

        response['data'] = book_type_counts 
        response['code'] = 0
        response['msg'] = "获取书籍类型数量成功"
    except Exception as e:
        print('发生未知错误:',e)
        response['code'] = 1
        response['msg'] = f"获取书籍类型数量失败，原因为{e}"
    finally:
        return JsonResponse(response)

def getAllBook(request):
    response = {}
    try:
        books_data = []
        books = BookBasic.objects.all()
        for book in books:
            cover_image_name = re.findall(covername_pattern,book.cover_image_url)[0]
            book_info = {
                'id': book.id,
                'title': book.title,
                'type': book.get_type_display(),
                'author': book.author,
                'description': book.description,
                'cover_image': cover_image_name,
            }
            books_data.append(book_info)
        # print('books_data: ',books_data)
        
        response['data'] = books_data
        response['code'] = 0
        response['msg']  = '获取所有书籍信息成功'
    except Exception as e:
        print(f'获取书籍时发生未知错误，原因为:{e}')
        response['code'] = 1
        response['msg']  = f'获取书籍时失败，原因为:{e}'
    finally:
        return JsonResponse(response)
    
def getBookInfo(request):
    response = {}
    try:
        bookID = request.POST.get('bookID')
        book_data = BookBasic.objects.get(id=bookID)
        
        # 格式化更新时间字符串
        update_time = book_data.updated_at.strftime('%Y-%m-%d %H:%M')
        
        # 获取对应书籍的所有章节
        chapters = book_data.bookchapter_set.all()  
        chapter_list = [{
            'id': chapter.order,
            'chapter_title': chapter.title,
        } for chapter in chapters]
        chapter_list.sort(key=lambda x: x['id'])
        
        # 截取封面的路径
        cover_image_name = re.findall(covername_pattern,book_data.cover_image_url)[0]
        
        book_data_dt = {
            'bookID':book_data.id,
            'bookTitle':book_data.title,
            'bookType':book_data.get_type_display(), #获取choices参数对应的名称
            'bookCover':cover_image_name,
            'bookAuthor':book_data.author,
            'bookSummary':book_data.description,
            'bookUpdateTime':update_time,
            'bookChapters':chapter_list
        }
        response['data'] = book_data_dt
        response['msg'] = '获取书籍详细内容成功'
        response['code'] = 0
        
    except Exception as e:
        print('获取书籍详细内容失败，原因为：',e)
        response['data'] = dict()
        response['code'] = 1
        response['msg'] = f"获取书籍详细内容失败！原因为{e}"

    return JsonResponse(response)

def getChapter(request):
    response = {}
    try:
        bookID = request.POST.get('bookID')
        chapterID = request.POST.get('chapterID')
        
        book = BookBasic.objects.get(id=bookID)
        try:
            chapter = book.bookchapter_set.get(order=chapterID)
        except ObjectDoesNotExist:
            response['code'] = 2
            response['msg'] = '该章节不存在'
            return JsonResponse(response)
        
        chapter_data_dt = {
            'bookTitle':book.title,
            'bookType':book.get_type_display(),
            'bookAuthor':book.author,
            'chapterTitle':chapter.title,
            'chapterContent':chapter.content.replace('\n\n','\n').lstrip('\n')
        }
        
        response['data'] = chapter_data_dt
        response['code'] = 0
        response['msg'] = '获取该章节成功'
    except Exception as e:
        print(f'获取该章节失败，原因为{e}')
        response['code'] = 1
        response['msg'] = f'获取该章节失败，原因为:{e}'
    
    return JsonResponse(response)

def recordInfo(request):
    user_id = request.POST.get('userID')
    book_id = request.POST.get('bookID')
    
    response = {}
    try:
        book = BookBasic.objects.get(id=book_id)
        user = User.objects.get(id=user_id)

        # 记录书本点击量
        book.click_count += 1
        book.save()
        
        # 记录用户信息
        UserBookClick.objects.create(
            book=book,
            user=user
        )
        
    except Exception as e:
        print( f'记录失败，原因为{e}')
        response['code'] = 1
        response['msg'] = f'记录失败，原因为{e}'
    
    return JsonResponse(response) 

def getallrecorddata(request):
    response = {}
    
    try:
        # 获取书本点击量
        click_count = {}
        books = BookBasic.objects.all()
        for book in books:
            click_count[book.title] = book.click_count
        response['click_count'] = click_count
        # print('click_count: ',click_count)
        
        # 获取用户特征(目前暂时只记录性别)
        gender_count = {'male':0,'female':0}
        for gender in User.objects.values('gender').annotate(Count('gender')):
            gender_count[gender['gender']] = gender['gender__count']
        # print('gender_count: ',gender_count)
        
        # 获取用户的点击时间
        date_count = {'0:00-06:00':0,'06:00-12:00':0,'12:00-18:00':0,'18:00-24:00':0}
        clicks = UserBookClick.objects.all()
        for click in clicks:
            clicked_at = click.clicked_at
            if 0 <= clicked_at.hour < 6:
                date_count['0:00-06:00'] += 1
            elif 6 <= clicked_at.hour < 12:
                date_count['06:00-12:00'] += 1
            elif 12 <= clicked_at.hour < 18:
                date_count['12:00-18:00'] += 1
            else:
                date_count['18:00-24:00'] += 1
        # print('date_count: ',date_count)
        
        response['data'] = {
            'click_count':click_count,
            'gender_count':gender_count,
            'date_count':date_count
            }
        response['code'] = 0
        response['msg'] = '获取记录数据成功'
        
        
    except Exception as e:
        print(f'获取记录数据失败，原因为{e}')
        response['code'] = 1
        response['msg'] = f'获取记录数据失败，原因为{e}'
    
    return JsonResponse(response) 