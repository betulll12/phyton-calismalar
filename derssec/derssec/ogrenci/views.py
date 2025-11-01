from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def ogrencianasayfa(request):
  template = loader.get_template('ogrenciana.html')
  return HttpResponse(template.render())


def ogrencilistesi(request):
    ogrenciliste = Talebe.objects.all()
    template = loader.get_template('ogrencilistesi.html')
    context ={
        'ogrencilistesi' : ogrenciliste,
    }
    return HttpResponse(template.render(context, request))


from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from .models import Talebe
class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Talebe
        fields = ['TC', 'AdiSoyadi',
                  'Aciklama']  
# Kullanmak istediğiniz alanları buraya ekleyin
def ekle(request):
    if request.method == 'POST': # POST = Gönderme işlemi
        form = OgrenciForm(request.POST)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritabanına kaydetme
            return redirect('ogrenciler')  #url name
    else: # GET işlemi
        form = OgrenciForm()
    return render(request, 'ogrenciekle.html', {'form': form})
