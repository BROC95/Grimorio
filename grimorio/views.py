
# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Grimorio
from .models import Mago
from .add_grimorio import asignacion


def getJson(body):
    my_json = body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    return data


@csrf_exempt
def envio(request):
    if request.method == "POST":
        body = request.body

        data = getJson(body)

        asSol = Mago()
        estado = False
        asSol.estado = estado
        if data['Name'] is not None and data['lastname'] is not None and data['age'] is not None:
            if data['Name'].isalpha() and data['lastname'].isalpha() and data['age'] > 0 and data['age'] < 100:
                asig = asignacion()

                asSol.Name = data['Name']
                asSol.lastname = data['lastname']
                asSol.age = data['age']
                asSol.id = asig.getId()
                asGri = Grimorio()

                asGri.grimo, asGri.front, asSol.magic_aff = asig.getMagic()
                estado = True
                asSol.estado = estado
                asGri.mago_id = asSol
                asSol.save()
                asGri.save()

                print(asSol)
                print(asGri)
            else:
                print("Negado Cadena vacia ")

        else:
            # asGri = Grimorio()
            print("Negado valores ", None)

        print(estado)

    return HttpResponse(request)


@csrf_exempt
def delete(request):
    print("entro")
    body = request.body
    data = getJson(body)
    mago = get_object_or_404(Mago, id=data['id'])
    print(mago.delete())
    return HttpResponse("Delete")


@csrf_exempt
def update(request):
    body = request.body
    data = getJson(body)
    asSol = Mago.objects.get(id=data['id'])
    # asSol.estado =estado
    asSol.Name = data['Name']
    asSol.lastname = data['lastname']
    asSol.age = data['age']
    asGri = Grimorio()
    asig = asignacion()  # Valores aleatorios de magia
    asGri.grimorio, asGri.front_page, asSol.magic_affinity = asig.getMagic()
    estado = True
    asSol.estado = estado
    asGri.mago_id = asSol
    asSol.save()
    asGri.save()

    return HttpResponse(asGri)


def index(request):
    if request.method == "GET":
        response = Grimorio.objects.all()
        data = {"Grimorio": list(response.values())}
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse("Not response")


def magos(request):
    if request.method == "GET":
        response = Mago.objects.all()
        data = {"Mago": list(response.values())}
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse("Not response")


def all(request):
    # a1 = Mago.objects.select_related('grimorio').all()
    a2 = Grimorio.objects.select_related('mago_id').all()
    print(a2.values())

    return HttpResponse(a2)
