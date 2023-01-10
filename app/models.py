from django.db import models

class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    tName = models.CharField(max_length=16, null=False, blank=False)
    profession = models.CharField(max_length=16)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.tName
