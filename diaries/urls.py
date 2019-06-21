from django.urls import path
from . import views

urlpatterns = [
    #トップ画面
    path(r'',views.top),
    #一覧画面
    path(r'diaries/',views.index,name='index'),
    #詳細画面
    path(r'diaries/<int:diary_id>/',views.detail, name='detail'),
    #作成画面
    path(r'diaries/create/',views.create,name='create'),
    #変更画面
    path(r'diaries/update/<int:diary_id>/',views.update,name='update')

]
