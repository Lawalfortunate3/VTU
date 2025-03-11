from django import forms

from vtp.models import Permode, Datatype


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
