from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.user.models import User 
from core.models import Producto

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','rut','email','password1','password2' ]
        labels = {'username':'Nombre de usuario','first_name':'Nombres','last_name':'Apellidos','rut':'RUT','email':'Correo Electrónico','password1':'Contraseña','password2':'Repetir Contraseña' }
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'    