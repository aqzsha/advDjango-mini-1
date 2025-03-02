from django.db import models

class Notification(models.Model):
    EMAIL = 'email'
    PUSH = 'push'
    TYPE_CHOICES = [
        (EMAIL, 'Email'),
        (PUSH, 'Push')
    ]

    recipient = models.EmailField()
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification_type} to {self.recipient}"