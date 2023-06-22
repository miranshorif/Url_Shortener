from django.db import models
from django.utils import timezone
from .utils import create_shortened_url

# Create your models here.

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(null=True,blank=True)
    time_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=7, unique=True, blank=True)
    
    class Meta:
        ordering = ["-created"]
        
    def __srt__(self):
        return f'{self.long_url} to {self.short_url}'
    
    def save(self,*args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        if self.last_access and (timezone.now() - self.last_access).days >= 365:
            self.short_url = ''
        self.last_access = timezone.now()
        super().save(*args, **kwargs)