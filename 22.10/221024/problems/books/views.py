from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method=='GET': # GET방식이라면
        books=Book.objects.all() # books_book에 있는 모든 데이터를 가지고 옴
        serializer=BookListSerializer(books,many=True) # BookListSerializer를 통해 books를 직렬화 함
        return Response(serializer.data) # serializer된 데이터를 JSON형태로 반환 함
    # Q 2.
    if request.method=='POST': # POST방식이라면
        serializer=BookSerializer(data=request.data) # 입력된 정보를 BookSerializer를 통해 직렬화 함
        if serializer.is_valid(raise_exception=True): #데이터가 유효하다면
            serializer.save() # 데이터를 데이터베이스에 저장함
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 생성된 정보를 JSON형태로 반환하고 201코드도 반환함



@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    if request.method=='GET': # GET방식이라면
        book=get_object_or_404(Book, pk=book_pk) # 게시글이 존재하면 데이터를 가져오고 존재하지 않으면 404코드를 반환함
        serializer=BookSerializer(book) # 가져온 데이터를 BookSerializer를 통해 직렬화 함
        return Response(serializer.data) # 직렬화 한 데이터를 JSON 형태로 반환함

    # Q 4.
    if request.method=='DELETE': # DELETE방식 이라면
        book=get_object_or_404(Book, pk=book_pk) # 게시글이 존재하면 데이터를 가져오고 존재하지 않으면 404코드를 반환함
        book.delete() # 게시글을 삭제함
        context={ 
            'delete' : book_pk
        } # 반환할 JSON 데이터 생성
        return Response(context) # 삭제후 생성한 JSON 데이터 반환
    # Q 5.
    if request.method=='PUT': # PUT방식 이라면
        book=get_object_or_404(Book, pk=book_pk) # 게시글이 존재하면 데이터를 가져오고 존재하지 않으면 404코드를 반환함
        serializer=BookSerializer(book,data=request.data) # 변경한 데이터를 직렬화 함
        if serializer.is_valid(raise_exception=True): # 데이터가 유효하다면
            serializer.save() # 데이터를 저장함
            return Response(serializer.data) # 직렬화 한 데이터를 JSON 형태로 반환함


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    comments=Comment.objects.all() # books_comment에 있는 모든 데이터를 가지고 옴
    serializer=CommentSerializer(comments, many=True) # CommentSerializer를 통해 comments를 직렬화 함
    return Response(serializer.data) # 직렬화 한 데이터를 JSON 형태로 반환함


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    book=Book.objects.get(pk=book_pk) # 댓글이 저장될 게시물을 호출함
    serializer=CommentSerializer(data=request.data) # 입력한 댓글 데이터를 직렬화 시킴
    if serializer.is_valid(raise_exception=True): # 데이터가 유효하다면
        serializer.save(book=book) # 댓글이 저장될 게시물과 함께 데이터를 저장함
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # 생성된 정보를 JSON형태로 반환하고 201코드도 반환함

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    if request.method=='GET': # GET방식이라면
        comment=get_object_or_404(Comment,pk=comment_pk) # 댓글이 존재하면 데이터를 가져오고 존재하지 않으면 404코드를 반환함
        serializer=CommentSerializer(comment) # 가져온 데이터를 CommentSerializer를 통해 직렬화 함
        return Response(serializer.data) # 직렬화 한 데이터를 JSON 형태로 반환함
    # Q 10.
    if request.method == 'DELETE': # DELETE방식이라면
        comment=get_object_or_404(Comment,pk=comment_pk) # 댓글이 존재하면 데이터를 가져오고 존재하지 않으면 404코드를 반환함
        comment.delete() # 댓글을 삭제함
        context={
            'delete' : comment_pk
        } # 반환할 JSON 데이터 생성
        return Response(context) # 삭제후 생성한 JSON 데이터 반환
