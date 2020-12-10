from django.shortcuts import render
from .models import Berita

# Create your views here.
def portofolio(request):
	berita = Berita.objects.all().order_by('-upload')
	context = {
		'semua_berita': berita,
	}
	return render(request, "portofolio/portofolio.html", context)