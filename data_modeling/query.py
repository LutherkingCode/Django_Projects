amerik = Continent.objects.create(name='Amerik')
ewop = Continent.objects.create(name='Ewòp')
afrik = Continent.objects.create(name='Afrik')
azi = Continent.objects.create(name='Azi')


ayiti = Country.objects.create(continent=amerik, name='Ayiti', population=11260000, area=27750)
kannada = Country.objects.create(continent=amerik, name='Kanada', population=37590000, area=9985000)
frans = Country.objects.create(continent=ewop, name='Frans', population=67060000, area=643801)
potigal = Country.objects.create(continent=ewop, name='Pòtigal', population=10280000, area=92212)
chin = Country.objects.create(continent=azi, name='Chin', population=1398000000, area=9597000)

kreyol = Language.objects.create(name='Kreyol')
franse = Language.objects.create(name='Fransè')
angle = Language.objects.create(name='Anglè')
potige = Language.objects.create(name='Pòtigè')
mandaren = Language.objects.create(name='Mandaren')

ayiti.languages.add(kreyol, franse)
kannada.languages.add(franse, angle)
frans.languages.add(franse)
potigal.languages.add(potige)
chin.languages.add(mandaren)


#peyi ki pale plis ke yon lang
peyi_yo = Country.objects.filter(languages__gt=1)
for peyi in peyi_yo:
    print(peyi.name)
    
#peyi ki pale yon sel lang
peyi_sel_lang= Country.objects.filter(languages__exact=1)
for peyi in peyi_sel_lang:
    print(peyi.name)

#peyi ki gen plis abitan
peyi_plis_abitan = Country.objects.order_by('-population').first()
print(peyi_plis_abitan.name)


#peyi ak plis gwo teritwa pa kontinan
kontinan_yo = Continent.objects.all()
for kontinan in kontinan_yo:
    pi_gwo_peyi= kontinan.country_set.order_by('-area').first()
    print(f"Continent: {kontinan.name}, Largest Country: {pi_gwo_peyi.name}, Area: {pi_gwo_peyi.area}")
    
    
    #peyi ki gen plis ke yon sel lang
 

