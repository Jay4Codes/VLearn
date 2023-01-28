from django.db import models
import os
# Create your models herec


def path_and_rename_for_resume(instance, filename):
    return os.path.join('Vlearn_'+filename)


class csvstorage(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	file = models.FileField(upload_to=path_and_rename_for_resume, null=True, blank=True)
	name = models.CharField(max_length=100, blank=True, default='')

