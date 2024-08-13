from backend.models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


