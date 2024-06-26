from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido, password=None, **extra_fields):
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        user = self.model(correo=correo, nombre=nombre, apellido=apellido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo, nombre, apellido, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(max_length=50, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=200)
    periodista = models.BooleanField(default=False)
    suscripcion = models.ForeignKey('suscripcion.Suscripcion', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set', 
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',  
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.correo
