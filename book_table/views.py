from django.shortcuts import render, HttpResponse


# Create your views here.
def index_view(request):
    return render(request, 'book_table/index.html')


def menu_view(request):
    return render(request, 'book_table/menu.html')
