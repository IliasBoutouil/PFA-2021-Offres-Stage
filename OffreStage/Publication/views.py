from django.shortcuts import get_object_or_404, redirect, render
from . models import Publication
from .forms import PublicationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

@login_required()
def OffreList(request):
    offres = Publication.objects.all().filter(type_publication='Offre').filter(etat=True).order_by('-date_publication')
    return render(request, 'Offres/offres.html', {'offres': offres})

@login_required()
def ShowOffre(request,pk):
    offre = get_object_or_404(Publication,id=pk)
    return render(request, 'Offres/offre.html', {'offre': offre})

@login_required()
def CreateOffre(request):
    if request.user.account_type=='recruteur':
        if request.method == "POST":
            form = PublicationForm(request.POST)
            if form.is_valid():
                offre = form.save(commit=False)
                offre.user_id = request.user.id
                offre.type_publication = 'Offre'
                offre.save()
                messages.success(request,'Offre créé avec succès, vous recevrez un email après la vérification et la confirmation de votre publication par notre équipe')
                return redirect('List Offres')
            else:
                messages.error(request,'Merci de vérifier tous les champs du formulaire ci-joint afin de créer votre offre de stage')
                return redirect('Create Offre')
        else:
            return render(request, 'Offres/create.html')
    return redirect('List Offres')


@login_required()
def EditOffre(request, pk):
        offre = get_object_or_404(Publication,id=pk)
        return render(request, 'Offres/edit.html', {'offre': offre})

@login_required()
def UpdateOffre(request, pk):
    offre = get_object_or_404(Publication,id=pk)
    form = PublicationForm(request.POST, instance=offre)
    if form.is_valid():
        form.save()
        return redirect('/Offres/')
    return render(request, 'Offres/edit.html', {'offre': offre})

@login_required()
def DestroyOffre(request, pk):
    offre = get_object_or_404(Publication,id=pk)
    if offre.user_id == request.user.id or request.user.is_admin:
        offre.delete()
        messages.success(request,'Offre supprimé avec succès')      
    return redirect("profile")    

######

@login_required()
def DemandeList(request):
    demandes = Publication.objects.all().filter(type_publication='Demande').filter(etat=True).order_by('-date_publication')
    return render(request, 'Demandes/demandes.html', {'demandes': demandes})

@login_required()
def ShowDemande(request,pk):
    demande = get_object_or_404(Publication,id=pk)
    return render(request, 'Demandes/demande.html',{'demande': demande})

@login_required()
def CreateDemande(request):
    if request.user.account_type=='student':
        if request.method == "POST":
            form = PublicationForm(request.POST)
            if form.is_valid():
                demande = form.save(commit=False)
                demande.user_id = request.user.id
                demande.type_publication = 'Demande'
                demande.save()
                messages.success(request,'Demande créé avec succès, vous recevrez un email après la vérification et la confirmation de votre publication par notre équipe')               
                return redirect('List demandes')
            else:
                messages.error(request,'Merci de vérifier tous les champs du formulaire ci-joint afin de créer votre demande de stage')
                return redirect('Create Demande')
        else:
            return render(request, 'Demandes/create.html')
    return redirect('List demandes')

@login_required()
def EditDemande(request, pk):
        demande = get_object_or_404(Publication,id=pk)
        return render(request, 'Demandes/edit.html', {'demande': demande})

@login_required()
def UpdateDemande(request, pk):
    demande = get_object_or_404(Publication,id=pk)
    form = PublicationForm(request.POST, instance=demande)
    if form.is_valid():
        form.save()
        return redirect('/demandes/')
    return render(request, 'Demandes/edit.html', {'demande': demande})

@login_required()
def DestroyDemande(request, pk):
    demande = get_object_or_404(Publication,id=pk)
    if demande.user_id == request.user.id or request.user.is_admin:
     demande.delete()
     messages.success(request,'Demande supprimé avec succès')        
    return redirect("profile")


def MailSender(request,subject,message,mail):
    try:
       send_mail(subject,message,'emsi.stages@gmail.com',[mail],fail_silently=False)
    except:
       messages.error(request,"Un problème est survenu lors de l'envoie d'email")
from datetime import date


@login_required()
def Approve(request, pk):
    demande = get_object_or_404(Publication,id=pk)
    if request.user.is_admin:
     demande.etat=True
     demande.save()
     messages.success(request,'Publication approuvée avec succès')
     message="Bonjour "+demande.user.first_name+",\nVotre publication "+demande.titre+" a été approuvé avec succés le "+str(date.today())+" vous pouvez la consulter dans n'importe quel moment.\nPour toutes informations contactez notre équipe sur : +212 522 232 427"
     subject='Publiction approuvée'
     MailSender(request,subject,message,demande.user.email)
    return redirect("profile")