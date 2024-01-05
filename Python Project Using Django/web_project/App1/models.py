from django.db import models

# Create your models here.
class studentInfo(models.Model):
    name = models.CharField(max_length=150)
    classDetails = models.IntegerField(null = True)
    address = models.TextField()

class libraryInfo(models.Model):
    name = models.CharField(max_length=150)
    classDetails = models.IntegerField(null = True)
    address = models.TextField()

class adminUser(models.Model):
    adminUserName = models.CharField(max_length=150)
    adminUserCountry = models.CharField(max_length=150)
    adminUsernumber = models.CharField(max_length=150)
    adminPassword = models.CharField(max_length=150)
    adminConfirmPassword = models.CharField(max_length=150)
    adminGender = models.CharField(max_length=150)
    adminEmail = models.CharField(max_length=150)
    adminStatus = models.CharField(max_length=150,default='Active')


class tenantUser(models.Model):
    tenantUserProfile = models.ImageField(upload_to="image/", null=True, blank=True, default="image/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg")
    tenantUserName = models.CharField(max_length=150)
    tenantUserCountry = models.CharField(max_length=150)
    tenantPassword = models.CharField(max_length=150)
    tenantConfirmPassword = models.CharField(max_length=150)
    tenantGender = models.CharField(max_length=150)
    tenantUsernumber = models.CharField(max_length=150)
    tenantUseremail = models.CharField(max_length=150)
    tenantadminUserAddress = models.CharField(max_length=150)
    tenantDocumentProof = models.ImageField(upload_to="image/", null=True, blank=True, default="image/no_image.jpg")
    monthRentDate = models.DateField()
    price = models.CharField(max_length=150)
    agreementStartDate = models.DateField()
    agreementEndDate = models.DateField()
    estatePic1 = models.ImageField(upload_to="image/", null=True, blank=True, default="image/no_image.jpg")
    estatePic2 = models.ImageField(upload_to="image/", null=True, blank=True, default="image/no_image.jpg")
    estatePic3 = models.ImageField(upload_to="image/", null=True, blank=True, default="image/no_image.jpg")
    estatePic4 = models.ImageField(upload_to="image/", null=True, blank=True, default="image/no_image.jpg")
    rentalType = models.CharField(max_length=150)
    adminStatus = models.CharField(max_length=150,default='Active')
    gymFacility = models.CharField(max_length=150)
    foodService = models.CharField(max_length=150)

    def __str__(self):
        return self.tenantUserName
     



    
