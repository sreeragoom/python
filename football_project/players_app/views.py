from django.http import HttpResponse
from django.shortcuts import render, redirect

from players_app.forms import PlayerForm
from players_app.models import Players


# Create your views here.
def index(request):
    player = Players.objects.all()
    return render(request, 'index.html', {'players': player})


def about(request, player_id):
    player = Players.objects.get(id=player_id)
    return render(request, 'about.html', {'about': player})


def add_players(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        market_value = request.POST.get('market_value')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        player = Players(name=name, age=age, market_value=market_value, desc=desc, img=img)
        player.save()
        return redirect('/')
    return render(request, "add.html")


def update(request,p_id):
    play = Players.objects.get(id=p_id)
    form = PlayerForm(request.POST or None, request.FILES, instance=play)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'play': play})


def delete(request,id):
    if request.method =="POST":
        player=Players.objects.get(id=id)
        player.delete()
        return redirect('/')
    return render(request,'delete.html')