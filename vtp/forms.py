from django import forms

from vtp.models import ReqData ,DataType
  

class DataForm(forms.ModelForm):
    class Meta: 
        model = ReqData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datatype'].queryset = DataType.objects.none()

        if 'network' in self.data:
            try:
                network_id = int(self.data.get('network'))
                self.fields['datatype'].queryset = DataType.objects.filter(network_id=network_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['datatype'].queryset = self.instance.network.datatype_set.order_by('name')

