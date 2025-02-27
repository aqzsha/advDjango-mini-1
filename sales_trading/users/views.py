from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsAdmin, IsTrader, IsSalesRep, IsCustomer
from users.tasks import send_welcome_email

class ExportUsersPDF(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="users.pdf"'
        
        pdf = canvas.Canvas(response, pagesize=letter)
        pdf.drawString(200, 750, "User List")
        pdf.drawString(200, 730, "----------------------------")

        y_position = 710  
        users = User.objects.all()
        for user in users:
            pdf.drawString(100, y_position, f"Username: {user.username}, Role: {user.get_role_display()}")
            y_position -= 20  
        
        pdf.showPage()
        pdf.save()
        return response

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
