# Importamos la funcion render, la clase TableroForm y las clases Casilla y tablero
from django.shortcuts import render
from .forms import TableroForm
from .Buscaminas import Casilla, Tablero

# Definimos la vista index que renderiza la plantilla 'index.html'.
def index(request):
    return render(request, 'tablero/index.html', {})

# Definimos la vista para manejar la creación y visualización de los tableros.
def tablero(request):

    tablero = None

    # Verificamos si la solicitud es un post cuando se envía el formulario.
    if request.method == 'POST':
        form = TableroForm(request.POST)

        # Verificamos si el formulario es válido.
        if form.is_valid():
            # Obtenemos los datos ingresados en el formulario.
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            num_minas = form.cleaned_data['num_minas']

            #Creamos una instancia de la clase Tablero con las dimensiones y el número de minas especificadas
            #Le añadimos el metodo mostrarTalero
            tablero = Tablero(filas, columnas, num_minas).mostrarTablero()

    # Si la solicitud no es un POST, se devuelve el formulario vacio
    else:
        form = TableroForm()

    # Si se genera un tablero, renderiza la plantilla 'muestra_tablero.html' con el formulario y el tablero.
    if tablero:
        return render(request, 'tablero/muestra_tablero.html', {'form': form, 'tablero': tablero})
    # Si no se genera un tablero, renderiza la plantilla 'crea_tablero.html' con el formulario.
    else:
        return render(request, 'tablero/crea_tablero.html', {'form': form})