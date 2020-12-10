from django import forms
from .models import PerkembanganAnak, BioData

class PerkembanganForm(forms.ModelForm):
	class Meta:
		model = PerkembanganAnak
		fields = ['berat', 'tinggi']

class BioDataForm(forms.ModelForm):
	class Meta:
		model = BioData
		fields = ['nama_ibu', 'tgl_lahir_ibu', 'gol_darah_ibu', 'telpon', 'alamat', 'nama_anak', 'tgl_lahir_anak', 'gol_darah_anak']