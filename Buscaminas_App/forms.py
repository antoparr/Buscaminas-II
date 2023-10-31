from django import forms
from django.core.exceptions import ValidationError

class tableForm(forms.Form):
    fila = forms.IntegerField(label='Fila:', min_value=1, max_value=20)
    columna = forms.IntegerField(label='Columna',min_value=1, max_value=15)
    minas = forms.IntegerField(label='Numero de minas')

    def clean(self):
        cleaned_data = super().clean()
        columna = cleaned_data.get('columna')
        fila = cleaned_data.get('fila')
        minas = cleaned_data.get('minas')

        if minas > ((fila * columna)/2):
            raise ValidationError(
                "Se ha producido un error. El número de minas debe ser menor o igual al numero de las casillas. "
            )
        return cleaned_data