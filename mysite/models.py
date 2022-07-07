from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pdate = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    class Meta:
        ordering = ('-pdate',)

    def __str__(self):
        return self.title

