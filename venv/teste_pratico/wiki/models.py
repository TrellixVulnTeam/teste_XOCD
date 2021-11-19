from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
       # www.meusite.com/wiki/post-1
    slug = models.SlugField(max_length=255, unique=True)


    STATS_CHOICES = (
        ('To do', 'To do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )
    status = models.CharField(max_length=25, choices=STATS_CHOICES)
    SETOR_CHOICES = (
        ('Admin', 'Admin'),
        ('Compras', 'Compras'),
        ('Mkt', 'Mkt'),
        ('Vendas', 'Vendas'),
        ('Produto', 'Produto'),
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
        ('Produção', 'Produção'),
        ('Pós-vendas', 'Pós-vendas'),
    )
    setor = models.CharField(max_length=25, choices=SETOR_CHOICES)
    
 

    nota = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
     return self.title
    def get_absolute_url(self):
        return reverse('wiki:detail', kwargs={'slug': self.slug})