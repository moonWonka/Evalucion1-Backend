import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def index(request):
    return render(request, 'template/index.html')

def usuario(request):
    documento = open("plantillas/template/usuario.html")
    plt = Template(documento.read())

    documento.close()

    ctx = Context({
        "nombre": "Juanita",
        "apellido": "Perez", 
        "edad": 25, 
        "fecha": datetime.datetime.now()
        })
        
    pagina = plt.render(ctx)

    return HttpResponse(pagina)

def productos(request):

    categorias = [
        {
            "nombre": "videojuegos",
            "items": [
                {
                    "producto": "FIFA 22",
                    "descripcion": "Simulador de fútbol",
                    "imagen" : "videojuegos/fifa2022.webp",
                    "precio": 49990
                },
                {
                    "producto": "PES 22",
                    "descripcion": "Simulador de fútbol",
                    "imagen" : "videojuegos/pes2022.webp",
                    "precio": 39990
                },
                {
                    "producto": "GTA V",
                    "descripcion": "Videojuego de acción y aventuras",
                    "imagen" : "videojuegos/gtav.webp",
                    "precio": 29990
                }
            ]
        },
        {
            "nombre": "ropa",
            "items": [
                {
                    "producto": "Camiseta",
                    "descripcion": "Camiseta de algodón para hombres",
                    "imagen" : "ropa/camisa.jpg",
                    "precio": 14990
                },
                {
                    "producto": "Pantalon",
                    "descripcion": "Pantalón de mezclilla para mujeres",
                    "imagen" : "ropa/pantalon.jpg",
                    "precio": 29990
                },
                {
                    "producto": "Zapatos",
                    "descripcion": "Zapatos de vestir para hombres",
                    "imagen" : "ropa/zapato.jpg",
                    "precio": 59990
                }
            ]
        },
        {
            "nombre": "juguetes",
            "items": [
                {
                    "producto": "Yoshi",
                    "descripcion": "Figura de acción de Yoshi con sonido",
                    "imagen" : "juguetes/saurio.jpg",
                    "precio": 62990
                },
                {
                    "producto": "Baby Yoda",
                    "descripcion": "Peluche Matel Star Wars Baby Yoda",
                    "imagen" : "juguetes/yoda.jpg",
                    "precio": 35000
                },
                {
                    "producto": "Peluche Wookie",
                    "descripcion": "Peluhe Star Wars Wookie de 25 cm",
                    "imagen" : "juguetes/wookie.jpg",
                    "precio": 27990
                }
            ]
        },
    ]
    
    nombreCategoria = request.GET.get('categoria')

    data = {}

    if nombreCategoria:
        
        for categoria in categorias:

            if categoria["nombre"] == nombreCategoria:

                data = {"categoria": categoria["nombre"],
                        "items": categoria["items"],
                        "fecha": datetime.datetime.now()
                        }
                break
                
    return render(request, 'template/productos.html', data)

# def juguetes(request):
#     return render(request, 'template/juguetes.html')

# def ropa(request):
#     return render(request, 'template/ropa.html')
