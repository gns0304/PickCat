from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid, os
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

def image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"images/{filename}"

class Kitchen(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    checkIn = models.PositiveSmallIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=False, blank=False)
    registeredAt = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, null=True, blank=True)

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
    favoriteKitchen = models.ManyToManyField(Kitchen)
    registeredAt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

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
    image = models.ImageField(upload_to=image_path, null=False, blank=False)
    like = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.post.cat.name} {self.post.title} {self.id}"



class CatMention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null=False, blank=False)
    mention = models.TextField(null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)


class KitchenMention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False, blank=False)
    mention = models.TextField(null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)


class EmergencyMention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False, blank=False)
    mention = models.TextField(null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, phoneNumber, longitude, latitude, address, password):
        if not email:
            raise ValueError("Email Needed")
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phoneNumber=phoneNumber,
            longitude=longitude,
            latitude=latitude,
            address=address
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phoneNumber=0,
            longitude=0,
            latitude=0,
            address=0,
            password=password
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user


   # temp = get_object_or_404(Cat, pk=1)
    # comm = temp.catmention_set.all()

    # 테스팅 코드
    # 삭제하지 말것

    # userObject = User.objects.first()
    # favoriteCats = userObject.favoriteCat.all()
    # favoriteKitchens = userObject.favoriteKitchen.all()
    #
    # tst = CatMention.objects.none()
    # for cat in favoriteCats:
    #     tst = tst.union(cat.catmention_set.all())
    #
    # for kitchen in favoriteKitchens:
    #     tst = tst.union(kitchen.kitchenmention_set.all())
    #
    # tst = tst.order_by('createdAt')
    #
    # return render(request,'chatting.html', {'cs' : tst})


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()
    #email, nickname, phoneNumber, longitude, latitude, address, password
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=20, null=False, blank=False, unique=True)
    phoneNumber = models.IntegerField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=200, null=True, blank=True)
    favoriteCat = models.ManyToManyField(Cat, null=True, blank=True)
    favoriteKitchen = models.ManyToManyField(Kitchen, null=True, blank=True)
    checkIn = models.PositiveSmallIntegerField(null=True, blank=True)
    feeding = models.PositiveSmallIntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']


class ImageTest(models.Model):
    image = models.ImageField(upload_to=image_path, null=False, blank=False)

    def __str__(self):
        return self.image.name
