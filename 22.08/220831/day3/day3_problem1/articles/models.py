from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=15)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.month}/{self.created_at.day}에 생성된 {self.id}번글 - {self.title} : {self.content}'
    
