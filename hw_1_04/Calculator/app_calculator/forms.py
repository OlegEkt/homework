from django import forms


class CalculationForm(forms.Form):
    num1 = forms.FloatField(label='Число 1')
    num2 = forms.FloatField(label='Число 2')
    num3 = forms.FloatField(label='Число 3')

    CHOICES = [('min', 'Минимум из трёх'), ('max', 'Максимум из трёх'), ('avg', 'Среднеарифметическое из трёх')]
    operation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)