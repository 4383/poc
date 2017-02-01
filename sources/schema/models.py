from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Entry(models.Model):
	name = models.CharField(max_length=250)
	internal_name = models.CharField(max_length=250)
	value = models.CharField(max_length=250)
	description = models.TextField(blank=True)

	def __str__(self):
		return '%s %s' % (self.name, self.value)


class Global(models.Model):
	name = models.CharField(max_length=250)
	version = models.CharField(max_length=50, default="0.1")
	section_name = models.CharField(max_length=250)
	entries = models.ManyToManyField(Entry)

	def __str__(self):
		return '%s %s' % (self.name, self.version)
	

class UserDefined(models.Model):
	name = models.CharField(max_length=250)
	version = models.CharField(max_length=50, default="0.1")
	section_name = models.CharField(max_length=250)
	section_name = models.CharField(max_length=250)
	user = models.ForeignKey(User)
	entries = models.ManyToManyField(Entry)

	def __str__(self):
		return '%s %s' % (self.name, self.version)


class Zone(models.Model):
	name = models.CharField(max_length=250)
	version = models.CharField(max_length=50, default="0.1")
	global_sections = models.ManyToManyField(Global)
	global_user = models.ManyToManyField(UserDefined)

	def __str__(self):
		return '%s %s' % (self.name, self.version)


class Schema(models.Model):
	name = models.CharField(max_length=250)
	version = models.CharField(max_length=50, default="0.1")
	zones = models.ManyToManyField(Zone)

	def __str__(self):
		return '%s %s' % (self.name, self.version)


class Warehouse(models.Model):
	name = models.CharField(max_length=250)
	user = models.ForeignKey(User)
	version = models.CharField(max_length=50, default="0.1")
	schemas = models.ManyToManyField(Schema)
	active = models.BooleanField(default=False)

	def __str__(self):
		return '%s %s' % (self.user, self.version)
