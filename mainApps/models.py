from django.db import models

# Create your models here.


class Kitchen(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    checkIn = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cat(models.Model):

    ISNEUTERED = (
        ('T', 'TRUE'),
        ('F', 'FALSE'),
        ('U', 'UNKNOWN')
    )
    GENDER = (
        ('M', "MALE"),
        ("F", "FEMALE"),
        ("U", "UNKNOWN")
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    breed = models.CharField(max_length=20, null=False, blank=False)
    isNeutered = models.CharField(max_length=1, choices=ISNEUTERED, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER, null=False, blank=False)
    feature = models.TextField(null=True, blank=True)
    favoriteKitchen = models.ForeignKey(Kitchen, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.name


class CatPost(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    article = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CatPhoto(models.Model):
    post = models.ForeignKey(CatPost, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)


class CatMention(models.Model):
    pass


