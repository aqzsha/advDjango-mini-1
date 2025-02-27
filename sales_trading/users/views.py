from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin, IsTrader, IsSalesRep, IsCustomer
from rest_framework.permissions import IsAuthenticated
from users.tasks import send_welcome_email

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdmin]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)  
