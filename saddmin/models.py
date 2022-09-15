
from django.db import models
class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

        
class stateName(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class propertyType(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(stateName, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=50, null=True)
    room = models.IntegerField(default=0, blank=False)
    beds = models.IntegerField(default=0, blank=False)
    baths = models.IntegerField(default=0, blank=False)
    squer_fit = models.IntegerField(default=0, blank=False)
    overview = models.CharField(max_length=1000, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    pro_img = models.ImageField(upload_to='propertyimage',blank=True, null=True)
    create_by = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name





class cityName(models.Model):
    name = models.CharField(max_length=100)
    state_id=models.ForeignKey(stateName, on_delete=models.CASCADE, null=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    
    def __str__(self):
        return self.author


class postEquiry(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    property_Id = models.ForeignKey(propertyType, on_delete=models.CASCADE)
    create_by = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.fullname