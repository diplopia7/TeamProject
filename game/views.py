from django.shortcuts import render


# Create your views here.
def game_info(request):
    return render(request, 'gameplay/game_info.html')


def main_menu(request):
    return render(request, 'gameplay/main_menu.html')


def character(request):
    return render(request, 'gameplay/character.html')


def story1(request):
    return render(request, 'gameplay/story1.html')


def story2(request):
    return render(request, 'gameplay/story2.html')


def story3(request):
    return render(request, 'gameplay/story3.html')


def 내정(request):
    return render(request, 'gameplay/내정.html')


def 전투(request):
    return render(request, 'gameplay/전투.html')
