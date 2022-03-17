from django import forms

from petstagram.profile_app.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'user':
                field.widget = forms.HiddenInput()
                field.required = False
            if hasattr(field, 'class'):
                field.widget.attrs['class'] += 'form-control'
            else:
                field.widget.attrs.update({'class': 'form-control'})


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'user':
                field.widget = forms.HiddenInput()
                field.required = False
            if name == 'birth_date':
                field.widget.attrs.update({'readonly': 'readonly'})
            if hasattr(field, 'class'):
                field.widget.attrs['class'] += 'form-control'
            else:
                field.widget.attrs.update({'class': 'form-control'})
