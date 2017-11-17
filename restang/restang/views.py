from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestangSerializer


class RestangView(APIView):
    def get(self, request):
        serializer = RestangSerializer()
        return Response(serializer.data)