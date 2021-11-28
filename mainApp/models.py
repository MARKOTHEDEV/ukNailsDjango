from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager




class UserManager(BaseUserManager):
    "this is what will manage the user"

    def create_user(self,email,password=None):
        "this is a custom function used to create my custom user"

        if password is None:
            raise ValueError("You Need To enter A Valid Password")

        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password):
        # function create a normal user and convert it to a Super User
        user = self.create_user(email,password)
        
        user.is_staff = True
        user.is_superuser=True
        user.save()

        return user

class User(PermissionsMixin,AbstractBaseUser):
    'This is Our Custom User The Whole Project will Use'

    email =      models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    # now i want to link the custom UserManager to Help me manage this my custom user
    objects =UserManager()

    def __str__(self):
        "String Rep of THe user"
        return f'{self.email}'




class Service(models.Model):
    "this will contain different types of services"
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    "one service can have different category"
    image = models.ImageField   (upload_to='service_category/',blank=True)
    name = models.CharField(max_length=500)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    duration = models.CharField(max_length=500,default='1 hour 35 minutes')
    info =models.TextField(default="More About this Product Like it Description")

    def __str__(self):
        return f'Service:"{self.service.name}" \t  CategoryName:"{self.name}"'


class ServiceCategoryAddOns(models.Model):
    # this will be located with tje ServiceCategory in the Admin Dashborad
    service_category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    

class Bookings(models.Model):
    name = models.CharField(max_length=500,blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    Total_amount_of_order = models.DecimalField(max_digits=20,decimal_places=2,blank=True)
    selected_addOns = models.TextField(default='..')
    service_category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)


    def __str__(self):return f'{self.name} booked for {self.service_category.name}'



class Testimonial(models.Model):
    person_name = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.person_name} wrote a testimonial"
        