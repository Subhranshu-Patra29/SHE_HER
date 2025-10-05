from django.db import models

class PickupLine(models.Model):
    CATEGORY_CHOICES = [
        ('romantic', 'Romantic'),
        ('techy', 'Techy + Romantic'),
    ]
    
    text = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category}: {self.text[:50]}..."
    
    class Meta:
        ordering = ['-created_at']