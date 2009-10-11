from django.db import models

class MakeUp(models.Model):
	css = models.TextField('CSS', null=True, blank=True)
	js = models.TextField('Javascript', null=True, blank=True)
	author = models.CharField(max_length=100)
	slug = models.CharField(max_length=255, unique=True)
	
	is_default = models.BooleanField(default=False)
