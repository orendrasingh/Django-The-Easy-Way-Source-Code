from django.shortcuts import render

from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status, permissions

from rest_framework.pagination import PageNumberPagination

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('mysite.add_blog'):
            return True
        return False


@api_view(['GET', 'PUT', 'DELETE'])
def blog_api_detail_view(request, pk=None):
    try:
        blog = Blog.objects.get(pk=pk)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog,
                                    data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(blog.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
@permission_classes([CustomPermission])
def blog_api_view(request):
    if request.method == "GET":

        paginator = PageNumberPagination()
        paginator.page_size = 1
        blog_objects = Blog.objects.all()
        result = paginator.paginate_queryset(blog_objects,
                                             request)

        # serializer = BlogSerializer(Blog.objects.all(),
        #                             many=True)
        serializer = BlogSerializer(result, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request,
                  'mysite/index.html')