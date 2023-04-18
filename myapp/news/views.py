from django.shortcuts import render, redirect
from  django.views.generic import DetailView, UpdateView, DeleteView
from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model=Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model=Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    success_url = '/news/'

class NewsDeleteView(DeleteView):
    model=Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Ошибка в заполнении'
    form = ArticlesForm()
    data = {'form':form,
            'error': error
            }

    return render(request, 'news/create.html', data)
