from firebase import firebase

firebase = firebase.FirebaseApplication('https://rito-python-crud.firebaseio.com/', None)
data =  { 'Nombre': 'Rito',
          'Dirección': "Las Gardenias",
          'Teléfono': 965795855,
          'email': "ritorito141516@gmial.com"
          }
#result = firebase.post('/rito-python-crud/Clientes/',data)

result = firebase.get('/rito-python-crud/Clientes/','')
print(result)

#firebase.put('/rito-python-crud/Clientes/-LhLzPi1919yPhm1ir6Y','Teléfono',989573672)
#print('updated')

#firebase.delete('/rito-python-crud/Clientes/','-LhLzPi1919yPhm1ir6Y')
#print('deleted')