from django.db import models

# Create your models here.
class Employee(models.Model):
	firstname = models.CharField(max_length=150)
	lastname = models.CharField(max_length=150, blank=True)
	address = models.CharField(max_length=150, blank=True)
	city = models.CharField(max_length=150, blank=True)
	st = models.CharField(max_length=150, blank=True)
	zipcode = models.CharField(max_length=20, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	fax = models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=150, blank=True)
    pdf = models.FileField(upload_to='pdfs/',blank=True)
	note = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	


	class Meta(object):
		unique_together = ("firstname", "lastname")
		verbose_name = "Contact"
		verbose_name_plural = "Contacts"
		
	def __str__(self):
	 	return "{} {}".format(self.firstname, self.lastname)