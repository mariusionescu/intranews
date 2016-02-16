from rest_framework.views import APIView
from rest_framework.response import Response
from wall.models import Component


class ComponentAPI(APIView):

    def get(self, request):
        components = Component.objects.all()
        return Response(components)


class CommentAPI(APIView):

    def get(self, request):
        comments = Component.objects.all()
        return Response(comments)