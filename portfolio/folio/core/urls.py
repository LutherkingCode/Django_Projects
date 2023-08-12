from django.urls import path, include
from . import views

# m ajoute liy kod sa pou evite server tonbe nan konfizyon ak chemen url li dwa pran le li resevwa yon reket
#piske chak nom app dwe inik sa fasilite server an jwenn modil ki gen  view ki korespon ak url lan (fonksyon) paske gen plizye aplikasyon anndan pwoje an)
app_name = 'core'

urlpatterns = [
    path('', views.byenvini,name='akey'),
    path('projects/', views.projects,name='projects'),
    path('skills/', views.skills,name='skills'),
    path('about/', views.about,name='about'),
]
