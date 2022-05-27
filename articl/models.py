from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):
    user = models.ForeignKey(to=User, null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cover = models.ImageField(upload_to=user_directory_path)#cover - картинка;
    book = models.FileField(upload_to='books/%Y-%m-%d/')# cover - картинка;

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



