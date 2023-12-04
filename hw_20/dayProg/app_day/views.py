from datetime import datetime, timedelta
from django.shortcuts import render


def programmers_day(request):
    today = datetime.today()
    day_of_year = 256
    programmers_day = datetime(today.year, 1, 1) + timedelta(days=day_of_year - 1)

    context = {
        'programmers_day': programmers_day.strftime("%A, %d %B")
    }

    return render(request, 'app_day/programmers_day.html', context)

