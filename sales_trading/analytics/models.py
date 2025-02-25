# analytics/models.py

from django.db import models

class AnalyticsReport(models.Model):
    REPORT_TYPE_CHOICES = (
        ('trading', 'Trading'),
        ('sales', 'Sales'),
    )

    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    generated_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()  # здесь можно хранить результаты анализа

    def __str__(self):
        return f"{self.get_report_type_display()} Report at {self.generated_at}"
