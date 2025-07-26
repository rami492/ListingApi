from api1.models import Listing
from api1.permissions import IsOwnerOrReadOnly, IsSelf
from api1.serializers import ListingSerializer, UserSerializer, LoginSerlializer, CreateUserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from django_filters.rest_framework import DjangoFilterBackend

from knox.auth import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelf]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'email', 'first_name', 'last_name']

class RegisterViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    
class ListingViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class LoginView(KnoxLoginView):
    http_method_names = ['post']
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerlializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'listings': reverse('listing-list', request=request, format=format),
    })