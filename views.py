from django.shortcuts import render
from .models import Articles
from django.shortcuts import redirect
from .models import Note

#def index(request):
#    return render(request, 'main/index.html')
def index(request):
    return render(request, 'main/index.html')
def Kalen(request):
    return render(request, 'main/Kalen.html') #Указываем путь до нужной функции
def Films(request):
    return render(request, 'main/Films.html')
def Prob2(request):
    return render(request, 'main/Prob2.html')
def Zam(request):
    return render(request, 'main/Zam.html')
def Finans(request):
    return render(request, 'main/Finans.html')
def side(request):
    return render(request, 'main/side.html')
def tren(request):
    return render(request, 'main/tren.html')
def bdnov(request):
    news = Articles.objects.order_by('title')
    return render(request, 'main/bdnov.html', {'news': news})
def add(request):
    return render(request, 'main/add_note.html')
def cursor(request):
    return render(request, 'main/cursor.html')

#def Rasp(request):
    #return HttpResponse("<h12>Тут будет расписание<h12>")

def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('index')
    return render(request, 'add_note.html')