from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import BioDataForm, PerkembanganForm
from . import models
from datetime import date
import datetime
from datetime import datetime as shit

# Create your views here.
def signin_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			print('gaiso login')
			return render(request, "user/signin.html", {'message':'Cannot login'})
	return render(request, "user/signin.html")

def signup_view(request):

	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username, email, password)

		if user:
			return redirect('auth:signin')
	return render(request, 'user/signup.html')

def insert_perkembangan(request):
	form = PerkembanganForm(request.POST or None)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			perkembangan = form.save(commit=False)
			perkembangan.user = User.objects.get(username=request.user)
			perkembangan.save()
			return redirect('auth:profile')

		else:
			print("not valid")
			print(form.errors)

	return render(request, 'user/testadd.html', context)

def profile(request):
	if models.BioData.objects.filter(user=request.user).exists():
		print('ada')
		context = {}
		update_biodata = models.BioData.objects.get(user=request.user)
		data = {
			'nama_ibu'     : update_biodata.nama_ibu,
			'tgl_lahir_ibu': update_biodata.tgl_lahir_ibu,
			'gol_darah_ibu': update_biodata.gol_darah_ibu,
			'telpon'	   : update_biodata.telpon,
			'alamat'       : update_biodata.alamat,
			'nama_anak'    : update_biodata.nama_anak,
			'tgl_lahir_anak': update_biodata.tgl_lahir_anak,
			'gol_darah_anak': update_biodata.gol_darah_anak,
		}
		form = BioDataForm(request.POST or None, initial=data, instance=update_biodata)
		context['form'] = form
		if request.method == "POST":
			
			form = form.save(commit=False)
			form.user = User.objects.get(username=request.user)
			form.save()
			return redirect('auth:profile')
		try:
			perkembangan = models.PerkembanganAnak.objects.filter(user=request.user)
			perkembangan_terbaru = models.PerkembanganAnak.objects.filter(user=request.user).order_by('-tanggal')[0].tanggal + datetime.timedelta(days=30)
			context['perkembangan'] = perkembangan
			context['hari_ini'] = date.today()
			context['perkembangan_terbaru'] = perkembangan_terbaru
			context['sisa_hari'] = perkembangan_terbaru - shit.now().date()
			return render(request, 'user/profile.html', context)

		except:
			pass



	else:
		print('gada')
		context = {}
		form = BioDataForm(request.POST or None)
		context['form'] = form
		if request.method == "POST":
			if form.is_valid():
				form = form.save(commit=False)
				form.user = request.user
				form.save()
				return redirect('auth:profile')
		try:
			perkembangan = models.PerkembanganAnak.objects.filter(user=request.user)
			perkembangan_terbaru = models.PerkembanganAnak.objects.filter(user=request.user).order_by('-tanggal')[0].tanggal + datetime.timedelta(days=30)
			context['perkembangan'] = perkembangan
			context['hari_ini'] = date.today()
			context['perkembangan_terbaru'] = perkembangan_terbaru
			context['sisa_hari'] = perkembangan_terbaru - shit.now().date()

		except:
			pass


		return render(request, 'user/profile.html', context)
	return render(request, 'user/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')