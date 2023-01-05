from django.shortcuts import render, redirect, HttpResponse
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages



# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def menu_view(request):
    return render(request, 'menu.html')


def add_reservation(request):

    form = ReservationForm()
    context = {
        'form': form    
    }

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reserv = form.save(commit=False)
            reserv.client = request.user
            reserv.save()
            messages.success(request, 'Reservation request submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    return render(request, 'table_booking.html', context)