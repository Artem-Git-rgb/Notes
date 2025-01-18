from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.IntegerField(default=0)
    action_dt = models.TextField(blank=True, null=True)
    is_last = models.BooleanField(default=False)
    is_in_recycle = models.BooleanField(default=False)
    last_update = models.TextField(blank=True, null=True)
    #models.TextField(models.DateTimeField(auto_now_add=True))


class Image(models.Model):
    img_id = models.AutoField(primary_key=True)
    note_id = models.IntegerField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)

