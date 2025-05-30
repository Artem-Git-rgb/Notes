from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.IntegerField(default=0)
    action_dt = models.TextField(blank=True, null=True)
    is_last = models.IntegerField(default=0)
    is_in_recycle = models.IntegerField(default=0)
    last_update = models.DateTimeField(blank=True, null=True)
    pic = models.ImageField(upload_to='pics', null=True)
