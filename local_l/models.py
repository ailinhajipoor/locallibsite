from django.db import models
from  django.urls import reverse
import  uuid


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='enter book genre')
    #
    # def __str__(self):
    #     return self.name


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

    # def get_absolute_url(self):
    #     return reverse('author-detail',args=[str(self.id)])
    def __str__(self):
        return '%s, %s ' %(self.first_name,self.last_name)


class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="help ID")
    book=models.ForeignKey('Book',on_delete=models.SET,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)

    Loan_Status=(
        ('m','main...'),
        ('o','on loan'),
        ('a','available...'),
        ('r','reserved...'),
    )
    status=models.CharField(max_length=1,choices=Loan_Status,blank=True,default='m',help_text="book availble")

    class meta():
        ordering=['due_back']
class Book(models.Model):
        title=models.CharField(max_length=200)
        author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
        summary=models.TextField(max_length=1000,help_text="enter description...")
        isbn=models.CharField('ISBN',max_length=13,help_text='13 <a href="www.google.com"')
        genre=models.ManyToManyField(Genre,help_text="select....")
        # def __str__(self):
        #     return self.title
        # def get_absolute_url(self):
        #     return reverse('book-detail',args=[str(self.id)])













