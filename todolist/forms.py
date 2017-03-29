from django import forms


class CreateTaskFrom(forms.Form):
    error_css_class = 'has-danger'
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
