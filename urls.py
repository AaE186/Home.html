from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #В файле views создан index, в котором текст, поэтому мы оттуда берем и подключаем сюда
    path('Главная', views.index),
    path('Календарь', views.Kalen), #В ковычках обозначается путь к окошку, типо как будет называться, а дальше после запятой
    path('Фильмы', views.Films), #<Название файла, с которого будем брать информацию> и саму функцию, текст или типо того
    path('Пробник2', views.Prob2),
    path('Зам', views.Zam),
    path('Финансы', views.Finans),
    path('side', views.side),
    path('бднов', views.bdnov),
    path('Трен', views.tren),
    path('add/', views.add_note, name='add_note'),
    path('cursor', views.cursor),

]
