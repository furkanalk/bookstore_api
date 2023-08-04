# bookstore_api

**********************************************
# Authentication:
Register: ``` POST ```
```
127.0.0.1:8000/api/auth/register/
```
```
{
    "username": "<username>",
    "email": "<email>",
    "password": "<password>"
}
```
Login: ``` POST ```
```
127.0.0.1:8000/api/auth/login/
```
```
{
    "username": "<username>",
    "password": "<password>"
}
```
Logout: ``` POST ```
```
127.0.0.1:8000/api/auth/logout/
```
**********************************************
# Available commands for all Users:
Shows all the books: ``` GET ```
```
127.0.0.1:8000/api/books/
```
**********************************************
# Available commands for Authenticated Users:

To borrow a book (pk is the book id): ``` BORROW ```
```
127.0.0.1:8000/api/books/borrow/<pk>
```
To return a borrowed book: ``` RETURN ```
> (the book must be borrowed first)
```
127.0.0.1:8000/api/books/borrow/<pk>
```
Check your borrowing history: ``` GET ```
```
127.0.0.1:8000/api/books/history/
```
**********************************************
# Available commands for Admin Users:

Show all the Users: ``` GET ```
```
127.0.0.1:8000/api/users/
```
Send a request to a specific User: ``` GET ``` ``` PUT ``` ``` DELETE ```
```
127.0.0.1:8000/api/users/<pk>
```
Send a request to a specific Book: ``` GET ``` ``` PUT ``` ``` DELETE ```
```
127.0.0.1:8000/api/books/<pk>
```
Add a new book: ``` POST ```
```
127.0.0.1:8000/api/books/add/
```
```
{
    "title": "<name of the book>",
    "author": "<name of the writer>",
    "publish_date": "<year>",
    "pages": "<number>"
}
```

