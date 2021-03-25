
import firebase_admin
from firebase_admin import credentials,firestore
import random
cred = credentials.Certificate("path/to/serviceAccountkey.json")
firebase_admin.initialize_app(cred)

firestore_db = firestore.client()


def marelab():

    for nodo in range(100000):
                    
        doc_ref = firestore_db.collection(u'Mercancias').document(u'Datos'+str(nodo))
        doc_ref.set({
            u'Naturaleza de carga':u'carga normal',
            u'Tipo de vehiculo': u'comioneta',
            u'Tipos de mercancia':u'mudanzas',
            })

def mercancia_update():

    doc_ref = firestore_db.collection(u'Mercancia').document(''++Datos')
    doc_ref.set({
        u'Naturaleza_de_carga':u'ligero',
        u'Tipo_de_vehiculo': u'automovil',
        })

def query_simple():

    documentos = firestore_db.collection(u'Mercancia')
    for datos in documentos.stream():
        print(f'{datos.id} => {datos.to_dict()}') 

def query_compleja():

    documentos = firestore_db.collection(u'Mercancia').where(u'Tipo_de_vehiculo',u'==','automovil')
    for datos in documentos.stream():
        print(f'{datos.id} => {datos.to_dict()}') 

#mercancia_update()

#query_simple()
query_compleja()
# snapshots = firestore_db.collection(u'Mercancias').document(u'Datos')
# snapshots2 = snapshots.get()

# print(snapshots2.to_dict())

