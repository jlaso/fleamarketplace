import json
import datetime
import models
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from serializers import MarketSerializer
from rest_framework import permissions

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    #url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

'''
def markets(request):
    markets = models.Market.filter()
    d = {'pk': markets.pk, 'address': '%s %s Spain' % (escuela.direccion, escuela.ciudad)}
    json_data = json.dumps(d)
    return HttpResponse(json_data, content_type='application/json')
'''

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def markets_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        queryset = models.Market.objects.all()
        serializer = MarketSerializer(queryset, many=True)
        return Response(serializer.data)
'''
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''