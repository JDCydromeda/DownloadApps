from django.db import models

# Create your models here.

class Apps(models.Model):
    Name = models.CharField(max_length=20)
    Image = models.FileField(upload_to="images")
    Description = models.CharField(max_length=500)
    Download = models.FileField(upload_to="apps")

    def __str__(self):
        return self.Name
