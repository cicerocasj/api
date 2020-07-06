from . import models
from . import serializers
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class ClientViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a client instance.

    list:
        Return all clients, ordered by most recently joined.

    create:
        Create a new client.

    delete:
        Remove an existing client.

    partial_update:
        Update one or more fields on an existing client.

    update:
        Update a client.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a product instance.

    list:
        Return all products, ordered by most recently joined.

    create:
        Create a new product.

    delete:
        Remove an existing product.

    partial_update:
        Update one or more fields on an existing product.

    update:
        Update a product.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a order instance.

    list:
        Return all orders, ordered by most recently joined.

    create:
        Create a new order.

    delete:
        Remove an existing order.

    partial_update:
        Update one or more fields on an existing order.

    update:
        Update a order.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CustomAuthToken(ObtainAuthToken, GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
