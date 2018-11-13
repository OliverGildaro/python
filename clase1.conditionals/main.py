#conditionals
#comparar dia de la semana

dia = 'lunes'
band = True

if dia == 'domingo':
      print('hoy es domingo')
elif dia == 'lunes' and True:
      print('hoy es lunes')
elif dia == 'martes' or False:
      print('hoy es martes')
else:
      print('hoy es sabado')

a = [1,2,3]
b = [1,2,3]

if a is b:
      print('the two objects are the same')
else:
      print('are not the same')#because a and b has diferent location memory

print(a is b)

print(id(a))
print(id(b))