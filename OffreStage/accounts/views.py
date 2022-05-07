from Publication.models import Publication
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from .models import Utilisateur
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, 'Merci de verifier vos informations de connexion')
            return redirect('Login')
    else:
        form = AuthenticationForm()
        return render(request, 'Auth/Login.html', {'form': form})


def Inscription(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST["password"])
            if request.POST['account_type'] == 'recruteur':
                user.account_type = 'recruteur'
            user.save()
            login(request, user)
            messages.success(
                request, 'Compte créé avec succés, Bienvenu sur notre plateforme Emsi Stagiaire')
            return redirect('home')
        else:
            messages.error(
                request, 'Merci de vérifier tous les champs du formulaire ci-joint afin de créer votre compte')
            return redirect('Inscription')
    else:
        form = UserCreationForm()
        return render(request, 'Auth/Inscription.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def display_students(request):
    students = Utilisateur.objects.all().filter(
        account_type='student').order_by('-date_joined')
    return render(request, 'Etudiants/etudiants.html', {'students': students})


@login_required()
def display_student(request, pk):
    student = get_object_or_404(Utilisateur, id=pk)
    if student.account_type == 'student':
        return render(request, 'Etudiants/etudiant.html', {'student': student})
    else:
        return redirect(request, 'home')


def home_screen(request):
    offres = Publication.objects.all().filter(
        type_publication='Offre').order_by('-date_publication')[:3]
    demandes = Publication.objects.all().filter(
        type_publication='Demande').order_by('-date_publication')[:3]
    return render(request, 'accueil.html', {'offres': offres, 'demandes': demandes})


@login_required()
def profile(request):
    if request.user.account_type == 'student':
        demandes = Publication.objects.all().filter(
            type_publication='Demande').filter(user_id=request.user.id).order_by('-date_publication')
        return render(request, 'Auth/profiles/student.html', {'demandes': demandes})
    elif request.user.account_type == 'recruteur':
        offres = Publication.objects.all().filter(
            type_publication='Offre').filter(user=request.user).order_by('-date_publication')
        return render(request, 'Auth/profiles/recruteur.html', {'offres': offres})
    else:
        publications = Publication.objects.all().order_by('-date_publication')
        users = Utilisateur.objects.all()
        return render(request, 'Auth/profiles/admin_panel.html', {'publications': publications, 'users': users})
