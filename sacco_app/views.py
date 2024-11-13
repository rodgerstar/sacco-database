from django.http import HttpResponse
from django.shortcuts import render

from sacco_app.models import Customer


# Create your views here.
def test(request):
    # c1 = Customer(first_name='John', last_name='Smith',
    #               email='johnsmith@gmail.com', dob='2000-11-21', gender='male')
    #
    # c1.save()
    #
    # c2 = Customer(first_name='ohn', last_name='Smith',
    #               email='ohnsmith@gmail.com', dob='2000-1-21', gender='female')
    #
    # c2.save()

    count = Customer.objects.count()

    c1 = Customer.objects.get(id=1)
    print(c1)

    return HttpResponse(f"ok, done we have {count} customers")



