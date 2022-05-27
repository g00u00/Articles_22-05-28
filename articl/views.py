from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

from django.views.generic import CreateView
from .forms import PostForm

class BookCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Post
    # Класс на основе которого будет валидация полей
    form_class = PostForm
    # Выведем все существующие записи на странице
    extra_context = {'books': Post.objects.all()}
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'articl/book_create.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = '/book/'

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articl/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'articl/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)# request.FILES - для выбора файла из формы
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'articl/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'articl/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'articl/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


from .models import Post
from django.core.files.storage import FileSystemStorage

'''def home_page(request):
    # получаем все значения модели
    data = Post.objects.all()
    return render(request, 'articl/home_page.html', {'data':data})'''

def home_page(request):
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'articl/home_page.html', {
            'file_url': file_url
        })
    return render(request, 'articl/home_page.html')

