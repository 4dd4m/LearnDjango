from django.db import models
from django.core.urlresolvers import reverse

def save_to(instance, filename):
    return "%/%" % (instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(
        null=True, 
        blank=True, 
        height_field="height_field",
        width_field="width_field"
        )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title

    def get_id(self):
        return "/detail/" + str(self.id) + "/"

    class Meta:
        ordering = ['-timestamp','-updated']

