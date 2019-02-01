from django.db import models

# Create your models here.
from django.conf import settings
from .validators import validate_content
from django.urls import reverse

class Posts(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content     = models.CharField(max_length=140, validators=[validate_content])
    liked       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    reply       = models.BooleanField(verbose_name='Is a reply?', default=False)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk":self.pk})

    class Meta:
        ordering = ['-timestamp']