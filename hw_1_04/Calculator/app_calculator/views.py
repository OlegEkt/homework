
from django.shortcuts import render
from .forms import CalculationForm


def calculate(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            num3 = form.cleaned_data['num3']
            operation = form.cleaned_data['operation']

            if operation == 'min':
                result = min(num1, num2, num3)
            elif operation == 'max':
                result = max(num1, num2, num3)
            else:
                result = (num1 + num2 + num3) / 3

            return render(request, 'result.html', {'result': result})
    else:
        form = CalculationForm()

    return render(request, 'calculate.html', {'form': form})