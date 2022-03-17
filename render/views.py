from django.shortcuts import render,redirect
from .models import employes,NewVideo,SivilNumber,YangiHodim,IbratRasm,Jamoa,UzgarishYangiliklar,KomisHodim,MaxallFuqorolar,Contact
def home(request):
    visible = True
    data = {
        'ishchilar':employes.objects.all(),
        'editor':SivilNumber.objects.all(),
        'YangiHodim': YangiHodim.objects.all(),
        'rasmlar': IbratRasm.objects.all(),
        'malumot': Jamoa.objects.all(),
        'uzgarishlar':UzgarishYangiliklar.objects.all(),
        'visible':visible
    }
    return render(request,'index.html',data)
def aloqa(request):
    visible = False
    return render(request,'aloqa.html')
def yangiliklar(request):
    visible = False
    data = {
        'Videolar':NewVideo.objects.all(),
        'YangiHodim': YangiHodim.objects.all(),
        'visible': visible
    }
    return render(request,'yangiliklar.html',data)

def UzTarih(request):
    visible = False
    return render(request,'UzTarih.html')

def malumotlar(request):
    visible = False
    data={
        'komis': KomisHodim.objects.all(),
        'maxxalla':MaxallFuqorolar.objects.all(),
        'visible': visible
    }
    return render(request,'malumotlar.html',data)
# Create your views here.
def send (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact(name=name,email=email,message=message).save()
        return redirect(to='/')
    return redirect(to='/')