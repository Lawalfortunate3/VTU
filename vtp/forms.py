from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from vtp.models import Permode, Datatype, AirtimeTran, Airtime



            # .... VALIDATION FORM....
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

            #  .... DATA FORM.....
class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Permode
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datatype'].queryset = Datatype.objects.none()

        if 'network' in self.data:
            try:
                network_id = int(self.data.get('network'))
                self.fields['datatype'].queryset = Datatype.objects.filter(network_id=network_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['datatype'].queryset = self.instance.network.datatype_set.order_by('name')


        if 'datatype' in self.data:
            try:
                datatype_id = int(self.data.get('datatype'))
                self.fields['datatype'].queryset = Datatype.objects.filter(datatype_id=datatype_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['dataplan'].queryset = self.instance.datatype.dataplan_set.order_by('name')


        #  .... AIRTIME FORM....


class AirtimeForm(forms.ModelForm):
    class Meta:
        model = AirtimeTran
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['airtime'].queryset = Airtime.objects.all()
