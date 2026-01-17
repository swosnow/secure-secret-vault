from django.db import models


class RequestLog(models.Model):
    method = models.CharField(max_length=10)
    url = models.TextField()
    body = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    response_status = models.IntegerField()
    response_body = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} {self.url} - {self.response_status} ({self.duration:.3f}s)"
