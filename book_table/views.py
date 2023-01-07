from django.shortcuts import render, redirect, HttpResponse, get_list_or_404
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from datetime import date


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def menu_view(request):
    return render(request, 'menu.html')


def add_reservation(request):

    


    if request.method == 'POST':
        form = ReservationForm(request.POST) 

        if form.is_valid():
            reserv = form.save(commit=False)
            reserv.client = request.user
            reserv.save()
            messages.success(request, 'Reservation request submitted successfully.')
        else:
            messages.error(request, 'The table is already booked.')
            reserv = form.instance.date

    try:
        reservations = get_list_or_404(Reservation)
    except:
        reservations = None
    
    form = ReservationForm()
    context = {
        'form': form,
        'reservations': reservations,
    }
    return render(request, 'table_booking.html', context)