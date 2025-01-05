from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=0)
    action_dt = models.TextField()
    is_last = models.BooleanField(default=False)
    is_in_recycle = models.BooleanField(default=False)
    last_update = models.TextField()
    #models.TextField(models.DateTimeField(auto_now_add=True))
