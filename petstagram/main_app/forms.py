from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from petstagram.main_app.models import Pet, PetPhoto


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user_profile',)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if hasattr(field, 'class'):
                field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if hasattr(field, 'class'):
                field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        exclude = ('likes',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if hasattr(field, 'class'):
                field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})


class PetEditForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if hasattr(field, 'class'):
                field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})
            

class PetDeleteForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if hasattr(field, 'class'):
                field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
