from django.db import models
import  uuid

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid1,help_text="help ID")
    book=models.ForeignKey('Book',on_delete=models.SET,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)