from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# функция для возврата картинки
from articl.views import home_page
from articl.views import home_page, BookCreate

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('admin/', admin.site.urls),
    # Url и функция, которая вернет картинку
    #path('', home_page),
    path('book/', BookCreate.as_view())


]
# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)