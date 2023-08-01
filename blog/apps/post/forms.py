from django import forms
from .models import Comentario, Post

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),  # Para darle un tamaño adecuado al campo de contenido
        }

        
class CrearArticuloForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['fecha_actualizacion'] 
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']               
        
        
