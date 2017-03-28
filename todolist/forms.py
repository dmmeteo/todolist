from django import forms


class CreateTask(forms.Form):
    error_css_class = 'has-danger'
    label_class = 'col-lg-2'
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
    )

    def clean_priority(self):
        data = self.cleaned_data['priority']
        if data not in ['normal', 'low', 'high', 'critical']:
            data = 'normal'
        return data
