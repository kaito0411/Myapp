from django.shortcuts import render,redirect
from diaries.models import Diary
# Create your views here.
def top(request):
    """トップ画面"""
    return render(request,'diaries/top.html')

def index(request):
    """ページ1"""
    diaries=Diary.objects.all()
    data_dictionary = {'diaries':diaries}
    return render(request,'diaries/index.html',data_dictionary)

def detail(request,diary_id):
    """ページの詳細"""
    diary = Diary.objects.get(id=diary_id)
    data_dictionary = {'diary':diary}
    if request.method =="POST":
        Diary.objects.filter(id=diary_id).delete()
        return redirect('index')
    else:
        return render(request,'diaries/detail.html',data_dictionary)

def create(request):
    if request.method == 'POST':
        diary = Diary.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            created = request.POST['created'])
        return redirect('detail',diary.id)
    else:
        return render(request,'diaries/create.html')

def update(request,diary_id):
    diary = Diary.objects.get(id=diary_id)
    if request.method=="POST":
        diary.title = request.POST.get('title')
        diary.detail = request.POST.get('detail')
        diary.created = request.POST.get('created')
        diary.save()
        return redirect('/diaries/'+str(diary.id))
    else:
        data = {'diary':diary}
        return render(request,'diaries/update.html',data)


