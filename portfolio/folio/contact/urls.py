from django.urls import path
from . import views


# m ajoute liy kod sa  epim ajoute atribi name lan nan path lan pou evite server tonbe nan konfizyon ak chemen url li dwe pran le li resevwa yon reket
#piske chak nom app dwe inik sa fasilite server an jwenn modil ki gen  view ki korespon ak url lan (fonksyon) paske gen plizye aplikasyon anndan pwoje an)

app_name = 'contact'
#avek chemen sa lew aksede ak  rasin aplikasyon contact lan ,l ap afiche fomile an
urlpatterns = [
    path(' ', views.contact_form,name='contact_formulaire'),
     
]