from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestangSerializer
from .models import RestangElements
from django.shortcuts import get_object_or_404

class RestangListView(APIView):
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

class RestangDetailView(APIView):
    def get(self, request, pk):
        restang = get_object_or_404(Restang, pk=pk)
        serializer = RestangSerializer(restang)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        restang = get_object_or_404(Restang, pk=pk):
        restang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)