from django.db import models

# Create your models here.
class admins(models.Model):
    firstname=models.CharField(verbose_name="firstname",max_length=100)
    secondname=models.CharField(verbose_name="secondname",max_length=100)
    password=models.CharField(verbose_name="password",max_length=100)
    companyname=models.CharField(verbose_name="password",max_length=100)
    username=models.CharField(verbose_name="phonenumber",max_length=100)
    email=models.EmailField(verbose_name="email")
    class Meta:
        db_table="admins"
    def __str__(self):
        return f"{self.firstname}{self.secondname}{self.password}{self.companyname}{self.username}{self.email}"
class vehicleregistations(models.Model):
    vehicle_iD=models.IntegerField(verbose_name="vehicle_id")
    make=models.CharField(verbose_name="make",max_length=100)
    car_model=models.CharField(verbose_name="car_model",max_length=100)
    Vin=models.IntegerField(verbose_name="vin")
    license=models.IntegerField(verbose_name="licence")
    class Meta:
        db_table="vehicleregistations"
    def __str__(self):
        return f"{self.vehicle_iD}{self.make}{self.car_model}{self.Vin}{self.license}"    
class driversreg(models.Model):
    firstname=models.CharField(verbose_name="firstname",max_length=100)
    Driver_id=models.IntegerField(verbose_name="Driver_id")
    license_Type=models.CharField(verbose_name="license_Type",max_length=100)
    Phonenumber=models.IntegerField()
    class Meta:
        db_table="driversreg"
    def __str__(self):
        return f"{self.firstname}{self.Driver_id}{self.license_Type}{self.Phonenumber}"
class routemangt(models.Model):
    vehicle_id=models.CharField(verbose_name="vehicle_id",max_length=100)
    start_location=models.CharField(verbose_name="start_location",max_length=100)
    end_location=models.CharField(verbose_name=" end_location",max_length=100)
    distance=models.IntegerField(verbose_name="distance")
    date=models.CharField(verbose_name="date",max_length=100)
    class Meta:
        db_table="routemangt"
    def __str__(self):
        return f"{self.vehicle_id}{self.start_location}{self.end_location}{self.distance}{self.date}"
class vehiclemaintance(models.Model):
    vehicle_id=models.CharField(verbose_name="vehicle_id",max_length=100)
    last_service=models.CharField(verbose_name="last_service",max_length=100)
    maintanance_type=models.CharField(verbose_name="maintanance_type",max_length=100)
    next_scheduled_service=models.CharField(verbose_name="next_scheduled_service",max_length=100)
    #date=models.DateField(verbose_name="date")
    class Meta:
        db_table="vehiclemaintance"
    def __str__(self):
        return f"{self.vehicle_id}{self.last_service}{self.maintanance_type}{self.next_scheduled_service}"
# driver_id=models.CharField(verbose_name="vehicle_id",max_length=100)
    #start_location=models.CharField(verbose_name="start_location",max_length=100)
    #end_location=models.CharField(verbose_name=" end_location",max_length=100)
    #date=models.DateField(verbose_name="date")
    #class Meta:
        #db_table="driver shift"
    #def __str__(self):
        #return f"{self.driver_id}{self.start_location}{self.end_location}{self.date}"
                    
    
    
    
    
    
    
    
    
    
    
    
 #paul codes   
   