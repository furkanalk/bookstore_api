from registration.models import User
from rest_framework import serializers
from .models import Book, Borrower

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email' , 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User(username = validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
            
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id' , 'title', 'author', 'publish_date', 'pages' , 'status']
        
class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['username', 'book', 'date', 'returndate']