from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
#
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
#
from .serializer import UserSerializer, BookSerializer, BorrowerSerializer
from registration.models import User
from .models import Book, Borrower
from django.utils import timezone, dateformat
        
# Show a list of all Users
@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def showUserList(request):
    if request.method == 'GET':
        Users = User.objects.all().order_by('id')
        serializer = UserSerializer(Users, many=True, context={'request': request})
        
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
    else:
        return HttpResponseNotAllowed(request.method)
    
    content = {'Users': serializer.data}
    return JsonResponse(content)

# Send a request to a User
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def RequestedUser(request,pk):
    theUser = get_object_or_404(User, id=pk)
    
    if request.method == 'GET':
        serializer = UserSerializer(theUser)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(theUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        theUser.delete()
        return Response("The User with ID NO = " + str(pk) + ", has been deleted.")
    
    else:
        return HttpResponseNotAllowed(request.method)

# Show a list of all Books
@api_view(['GET'])
def showBookList(request):
    if request.method == 'GET':
        Books = Book.objects.all().order_by('id')
        serializer = BookSerializer(Books, many=True, context={'request': request})
        
    else:
        return HttpResponseNotAllowed(request.method)
    
    content = {'Books': serializer.data}
    return JsonResponse(content)  

# Add a new Book
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addBooks(request):     
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    else:
        return HttpResponseNotAllowed(request.method)

# Send a request to a Book
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def RequestedBook(request,pk): 
    theBook = get_object_or_404(Book, id=pk)
    
    if request.method == 'GET':    
        serializer = BookSerializer(theBook)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(theBook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        theBook.delete()
        return Response("The Book with ID NO = " + str(pk) + ", has been deleted.")
    
    else:
        return HttpResponseNotAllowed(request.method)

# Borrow or return a book
@api_view(['BORROW', 'RETURN'])
@permission_classes([IsAuthenticated])
def borrowBooks(request,pk): 
    theBook = get_object_or_404(Book, id=pk)
    
    if request.method == 'BORROW':
        if theBook.status == theBook.STATUS_CHOICES[1][0]:
            return Response("'" + theBook.title + "' is already borrowed, please choose another one.")
        else:
            theBook.status = theBook.STATUS_CHOICES[1][0]
            theBook.save()
            user = User.objects.get(id = request.user.id)
            book_ = Book.objects.get(id = pk)
            formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            Borrower.objects.create(username = user, mail= request.user.email, 
            date = formatted_date, book = book_, book_title = theBook.title, book_author = theBook.author )
            return Response("You have successfully borrowed '" + theBook.title + "'.")
        
    elif request.method == 'RETURN':
        if theBook.status == theBook.STATUS_CHOICES[1][0]:
            theBook.status = theBook.STATUS_CHOICES[2][0]
            theBook.save()
            
            formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            data = Borrower.objects.filter(book_id = pk).latest('id')
            if data is not None:
                data.returndate = formatted_date
                data.save(update_fields=['returndate'])
            
            return Response("You have successfully returned '" + theBook.title + "'.")
        else:
            return Response("You haven't borrowed '" + theBook.title + "' yet.")
    else:
        return HttpResponseNotAllowed(request.method)
    
# Show the Users their Borrowing History
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def borrowingHistory(request):
    if request.method == 'GET':
        try:
            BorrowerHistory = Borrower.objects.filter(username_id = request.user.id).order_by('id')
        except:
            BorrowerHistory = None
            
        serializer = BorrowerSerializer(BorrowerHistory, many=True, context={'request': request})
    else:
        return HttpResponseNotAllowed(request.method)
    
    if not serializer.data:
        content = {'Your Book History': 'You haven not borrowed any books yet'}
    else:
        content = {'Your Book History': serializer.data}
    return JsonResponse(content)