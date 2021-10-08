from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ClientSerializer, OperationSerializer
from .models import Client, Operation
from .tasks import check_1000, check_0


class ClientViewSet(viewsets.ModelViewSet):
    model = Client
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class AddictOperationViewSet(viewsets.ModelViewSet):
    model = Operation
    serializer_class = OperationSerializer
    queryset = Operation.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            client_id = serializer.validated_data.get('client_id')
            Client.objects.filter(id=client_id).update(
                balance=F('balance') + serializer.validated_data.get('summary'))
            check_0.delay(client_id)
            check_1000.delay(client_id)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SubtractOperationViewSet(viewsets.ModelViewSet):
    model = Operation
    serializer_class = OperationSerializer
    queryset = Operation.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            client_id = serializer.validated_data.get('client_id')
            Client.objects.filter(id=client_id).update(
                balance=F('balance') - serializer.validated_data.get('summary'))
            check_0.delay(client_id)
            check_1000.delay(client_id)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
