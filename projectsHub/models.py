from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    picture= CloudinaryField('picture')
    projecturl= models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    posted= models.DateField(auto_now_add=True )
    def save_posts(self):
        self.user
    def delete_posts(self):
        self.delete()
    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()

