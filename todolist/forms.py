from django import forms
from django.core.exceptions import ValidationError


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

    # needless clean
    def clean_priority(self):
        data = self.cleaned_data['priority']
        if data not in [a[0] for a in self.options]:
            raise ValidationError(
                'Invalid choice: %(value)s',
                code='invalid',
                params={'value': data},
            )
        return data
