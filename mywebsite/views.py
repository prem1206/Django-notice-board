from django.shortcuts import render
from myapp.models import Board

def home(request):
    board = Board.objects.all()
    context = {'board': board}
    return render(request, "home.html",context)