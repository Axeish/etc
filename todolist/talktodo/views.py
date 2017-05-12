from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'name':'Axe', 'todos':todos
    }
    return render(request, 'index.html',context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        checked = is_private = request.POST.get('checked', False);
        todo = Todo(title=title, text=text,checked=checked)
        todo.save()
        return redirect('/todo')

    else:
        return render(request, 'add.html')