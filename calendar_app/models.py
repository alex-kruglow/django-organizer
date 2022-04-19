from django.db import models


class toDo(models.Model):
    createTime = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    changeTime = models.DateTimeField(
        auto_now=True
    )
    link = models.DateField()
    username = models.ForeignKey(
        'auth.User',
        related_name='rel_from_set',
        on_delete=models.CASCADE,
    )
