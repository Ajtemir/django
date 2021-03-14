from django.shortcuts import render
import MySQLdb

def book_list(request):
    db=MySQLdb.connect(user='me',
    db='mydb',passwd='secret',
    host='localhost')
    cursor=db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names=[row[0] for row in cursor.fetchall()]
    db.close()
    return render(request,'book_list.html',('names':names))

from django.shortcuts import render
from mysite.books.models import BOOK

def book_list(request):
    books=Book.objects.order_by('name')
    return render(request,'book_list.html',('books':books))



from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)