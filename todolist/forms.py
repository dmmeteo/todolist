from django import forms


class CreateTask(forms.Form):
    error_css_class = 'has-danger'
    required_css_class = 'required'
    options = (
        ('normal', 'normal'),
        ('low', 'low'),
        ('high', 'high'),
        ('critical', 'critical')
    )

    description = forms.CharField(
        label=False,
        max_length=300,
        widget=forms.TextInput(attrs={"placeholder": "Task description"})
    )
    priority = forms.ChoiceField(
        label=False,
        choices=options,
        widget=forms.Select(attrs={"class": "col-6"})
    )

    def clean_priority(self):
        data = self.cleaned_data['priority']
        print data
        if data not in ['normal', 'low', 'high', 'critical']:
            data = 'normal'
        return data
