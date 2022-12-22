from email.policy import default
from django.forms import ModelForm
from .models import modretur,students



class modraturForm(ModelForm):
        class Meta:
           model = modretur
           fields = '__all__'
           exclude = ['gender', 'Email']
       


class studentForm(ModelForm):
      class Meta:
           model = students
           fields = '__all__'
           