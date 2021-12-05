from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Project(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )

    title = models.CharField(max_length=100)
    topics = models.CharField(max_length=200)
    techs = models.CharField(max_length=300, default='python')
    details = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

class Comment(models.Model):

    project=models.ForeignKey(
            Project,
            on_delete=models.CASCADE,
            related_name='comments'
        )
    comment=models.TextField()
    author=models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    # active=models.BooleanField(default=False)

    def __str__(self):
        return self.comment

    class Meta:
        ordering=['created']