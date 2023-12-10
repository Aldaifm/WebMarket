from django.shortcuts import render, redirect

from item.models import Category, Item, Video

from .forms import SignupForm, VideoForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    video=Video.objects.all()
    return render(request, 'core/index.html',{
		'categories': categories,
		'items': items,
        'video': video,
	})

def contact(request):
    # Título predefinido
    titulo = "Muestra de la granja"
    
    # Crea una instancia del modelo Video y asigna el archivo manualmente
    video = Video(titulo=titulo)
    video.archivo = '/pollitos.mp4'  # Ruta al archivo en tu servidor
    video.save()

    # Obtén la URL del archivo y pásala a la plantilla
    video_url = video.archivo.url

    return render(request, 'core/contact.html', {'titulo': titulo, 'video_url': video_url})
  
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

