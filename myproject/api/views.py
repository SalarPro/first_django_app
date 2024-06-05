from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post
from .serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def getData(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def new_post(request):
    serializer = PostSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)