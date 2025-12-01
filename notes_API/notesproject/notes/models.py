from django.db import models

# Create your models here.
class Tag(models.Model):
    
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default="#3B82F6")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        

class Note(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        
        ordering = ['-created_at']
    