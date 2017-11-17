from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestangSerializer
from .models import RestangElements

class RestangView(APIView):
    def get(self, request):
        todos = RestangElements.objects.all()
        serializer = RestangSerializer(todos, many=True)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = RestangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(None)
