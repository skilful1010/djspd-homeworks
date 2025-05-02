from django.db import models


class Client(models.Model):
    #id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    mileage = models.IntegerField()
    volume = models.DecimalField(max_digits=2, decimal_places=1)
    body_type = models.CharField(choices=BODY_TYPE_CHOICES, max_length=20)
    drive_unit = models.CharField(choices=DRIVE_UNIT_CHOICES, max_length=20)
    gearbox = models.CharField(choices=GEARBOX_CHOICES, max_length=20)
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.model} | {self.fuel_type} | {self.gearbox}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} | {self.car.model} | {self.created_at}'
