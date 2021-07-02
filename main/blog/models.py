from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
