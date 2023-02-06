from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.
def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_details = "\n".join(f"{pokemon.id} - {pokemon.name} - {pokemon.type}")
    return HttpResponse(f"<b>{pokemon_details}</b>")


def get_pokemon_list(request):
    pokemons = Pokemon.objects.all()
    pokemon_list = "\n".join(f"<p>{pokemon.id} - {pokemon.name} - {pokemon.type}</p>" for pokemon in pokemons)
    return HttpResponse(f"<b>{pokemon_list}</b>")