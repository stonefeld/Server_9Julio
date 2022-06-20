import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from usuario.models import Deuda


@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        try:
            deudaMax = request.POST.get('deuda')
            deuda = Deuda.objects.all().last()
            deuda.deuda = deudaMax
            deuda.save()

            media_root = settings.MEDIA_ROOT
            location = os.path.join(media_root, 'saldos.xls')

            if os.path.exists(location):
                os.remove(location)

            try:
                uploaded_file = request.FILES['file']
                fs = FileSystemStorage()
                name = fs.save('saldos.xls', uploaded_file)
                context['url'] = fs.url(name)
                deuda.save()

                return redirect('usuario:cargarDB')

            except:
                context = {
                    'deuda': str(Deuda.objects.all().last().deuda),
                    'title': 'Subir archivos'
                }
                messages.warning(request, 'Debe subir un archivo')

        except:
            context = {
                'deuda': str(Deuda.objects.all().last().deuda),
                'title': 'Subir archivos'
            }
            messages.warning(request, 'Debe especificar una deuda máxima')

    elif request.method == 'GET':
        try:
            context = {
                'deuda': str(Deuda.objects.all().last().deuda),
                'title': 'Subir archivos'
            }

        except:
            deuda = Deuda(deuda=300)
            deuda.save()
            context = {
                'deuda': str(Deuda.objects.all().last().deuda),
                'title': 'Subir archivos'
            }

    return render(request, 'draganddrop/upload.html', context)
