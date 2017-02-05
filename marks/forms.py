from django import forms
from django.forms import formset_factory

from .models import Teacher, Marks

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={
                        'class': 'mdl-textfield__input',
                        'type': 'email',
                        'id': 'user'
                }),
            'password': forms.PasswordInput(attrs={
                        'class': 'mdl-textfield__input',
                        'type': 'password',
                        'id': 'password'
                })
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'first_sessional', 'second_sessional', 'internal_assessment']

MarksFormSet = formset_factory(MarksForm)