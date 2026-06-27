from django.shortcuts import render
import random


def memory_game(request):
    marques = [
        'BMW', 'Toyota', 'Mercedes', 'Tesla',
        'Ford', 'Land Rover', 'Audi', 'Cupra'
    ]
    paires = marques + marques
    random.shuffle(paires)

    context = {
        'marques': paires,
        'grid_cols': 4,
        'total_paires': len(marques),
    }
    return render(request, 'game/memory_game.html', context)
