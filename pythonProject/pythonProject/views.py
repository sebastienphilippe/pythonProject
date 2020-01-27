from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def projet(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Hola que tal</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
        <form>
            <label for="name">Enter your name: </label>
            <input type="text" name="name" id="name" required>
        </form>

    """)