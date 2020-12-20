from django.db import models
from django.forms import ModelForm
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    authorname = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Articleform(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
