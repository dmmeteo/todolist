from django import forms


class CreateTask(forms.Form):
    error_css_class = 'has-danger'
    required_css_class = 'required'

    priority = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Task priority"}))
    description = forms.CharField(label=False, max_length=300, widget=forms.TextInput(attrs={"placeholder": "Task description"}))

    def clean_priority(self):
        return self.cleaned_data['priority']