from django.shortcuts import render, redirect, HttpResponse, get_list_or_404, get_object_or_404
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

def mybooking_view(request):
    try:
        reservations = get_list_or_404(Reservation, client = request.user)
    except:
        reservations = None
    
    form = ReservationForm()
    context = {
        'reservations': reservations,
    }
    return render(request, 'mybooking.html', context)

def edit_booking(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance = reservation)
        if form.is_valid():
            form.save()
        return redirect('mybooking_view')

    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)

