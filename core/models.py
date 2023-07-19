from django.db import models
from django.contrib.auth.models  import User


class Task(models.Model): 
    user  = models.ForeignKey(User , on_delete=models.CASCADE , related_name='tasks')
    task  = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True , null=True  , blank=True)
    update_at = models.DateTimeField(auto_now=True , null=True  , blank=True)
    finish_at = models.DateTimeField(null=True , blank=True)

    def __str__(self ) : 
        return str(self.user.username)
