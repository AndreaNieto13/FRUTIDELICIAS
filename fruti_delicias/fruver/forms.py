from django import forms
from .models import Categorias, Productos
from django.forms import ModelChoiceField

#creamos el formulario a partir el modelo
class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
        
#creamos el formulario a partir el modelo
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['cate_id'].queryset = Categorias.objects.all()
        self.fields['cate_id'].widget.attrs.update({'class': 'form-control'}) 
