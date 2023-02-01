from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name =models.CharField(max_length=50)
    dep_description=models.TextField()

    def __str__(self) -> str:  # its for show the doctor department in data creation
        return self.dep_name


class Doctors(models.Model):
    doc_name=models.CharField(max_length=250)
    doc_spec=models.CharField(max_length=250)
    dep_name=models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
