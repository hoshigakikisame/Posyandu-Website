from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class BioData(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user',null=True, blank=True)
	nama_ibu       = models.CharField(max_length=100) 
	tgl_lahir_ibu  = models.DateField()
	
	gol_darah = (
		('A','A'),
		('B', 'B'),
		('O','O'),
		('AB','AB'),
	)

	gol_darah_ibu  = models.CharField(max_length=2, choices=gol_darah, default='A') 
	telpon         = models.CharField(max_length=20)
	alamat         = models.CharField(max_length=100)

	nama_anak      = models.CharField(max_length=100)
	tgl_lahir_anak = models.DateField()
	gol_darah_anak = models.CharField(max_length=2, choices=gol_darah, default='A')

	def save(self, *args, **kwargs):
		super(BioData, self).save(*args, **kwargs)
		super().save()

	def __str__(self):
		return "Biodatanya {}".format(self.user)

class PerkembanganAnak(models.Model):
	user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tanggal = models.DateField(auto_now_add=True)
	berat = models.PositiveIntegerField()
	tinggi = models.PositiveIntegerField()
	
	def __str__(self):
		return "Perkembangan anak dari {}".format(self.user)

	def save(self, *args, **kwargs):
		super(PerkembanganAnak, self).save(*args, **kwargs)
		super().save()

class PesanStaff(models.Model):
	isi = models.TextField()
	untuk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return "Pesan untuk {}".format(self.untuk)

	def save(self, *args, **kwargs):
		super(PesanStaff, self).save(*args, **kwargs)
		super().save()
