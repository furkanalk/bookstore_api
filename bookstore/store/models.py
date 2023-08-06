from django.db import models
from registration.models import User

class Book(models.Model): 
    
    DRAFT = 'Hidden'
    INUSE = 'in Use'
    AVAILABLE = 'Available'

    STATUS_CHOICES = (
        (DRAFT, 'Hidden'),
        (INUSE, 'in Use'),
        (AVAILABLE, ' Available'),
    )
        
    title = models.CharField(max_length=50)
    author = models.TextField(max_length = 50)
    publish_date = models.TextField(max_length = 50)
    pages = models.TextField(max_length=20, blank=True)
    #price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=AVAILABLE)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Books'
        
    def __str__(self):
        return self.title
    
    def get_author_name(self):
        return self.author
    
class Borrower(models.Model):
    class Meta:
        verbose_name_plural = 'Borrowers'
        
    username= models.ForeignKey(User, related_name='borrower_username', on_delete=models.SET_NULL, null=True)
    mail = models.CharField(max_length=225)
    date = models.CharField(default = None, max_length=30, null = True)
    returndate = models.CharField(default = None, max_length=30, null = True)
    book = models.ForeignKey(Book, related_name='borrower_book', on_delete=models.SET_NULL, null=True)
    book_title = models.CharField(max_length=225, default=None, null = True)
    book_author = models.CharField(max_length=225, default=None, null = True)

    def __str__(self):
        return str(self.book)