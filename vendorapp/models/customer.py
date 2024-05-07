from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=200)
    
    def isexist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    @staticmethod
    def getemail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            pass