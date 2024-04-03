from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.TextField()
    introduction = models.TextField()
    date_time = models.DateTimeField()
    views = models.DecimalField(decimal_places=1, max_digits=10, default=3.2)
    body = models.TextField()
    body1 = models.TextField()
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    body5 = models.TextField(blank=True, null=True)
    body6 = models.TextField(blank=True, null=True)
    body7 = models.TextField(blank=True, null=True)
    body8 = models.TextField(blank=True, null=True)
    body9 = models.TextField(blank=True, null=True)
    body10 = models.TextField(blank=True, null=True)
    posted_by = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_time']
        
class Hottest(models.Model):
    title = models.CharField(max_length=120)
    image = models.TextField()
    introduction = models.TextField()
    date_time = models.DateTimeField()
    views = models.DecimalField(decimal_places=1, max_digits=10)
    body = models.TextField()
    body1 = models.TextField()
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    body5 = models.TextField(blank=True, null=True)
    body6 = models.TextField(blank=True, null=True)
    body7 = models.TextField(blank=True, null=True)
    body8 = models.TextField(blank=True, null=True)
    body9 = models.TextField(blank=True, null=True)
    body10 = models.TextField(blank=True, null=True)
    posted_by = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_time']
    