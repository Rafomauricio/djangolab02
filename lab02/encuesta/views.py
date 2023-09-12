from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)
def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)
def calcular(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operacion = request.POST.get('operacion')

        if operacion == 'suma':
            resultado = num1 + num2
            operacion_text = 'suma'
        elif operacion == 'resta':
            resultado = num1 - num2
            operacion_text = 'resta'
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
            operacion_text = 'multiplicación'
        else:
            resultado = 0
            operacion_text = 'operación no válida'

        resultado_text = f'El resultado de {num1} {operacion_text} {num2} = {resultado}'
        return HttpResponse(resultado_text)

    return render(request, 'encuesta/calculadora.html')
def calcular_cilindro(request):
    if request.method == 'POST':
        # Obtener los valores de altura y diámetro del formulario
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])

        # Calcular el volumen del cilindro (fórmula: π * radio^2 * altura)
        radio = diametro / 2
        volumen = 3.14159265359 * (radio ** 2) * altura

        return render(request, 'encuesta/cilindro_resultado.html', {'volumen': volumen, 'altura': altura, 'diametro': diametro})

    return render(request, 'encuesta/cilindro.html')