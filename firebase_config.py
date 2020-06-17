import firebase_admin
from firebase_admin import credentials, firestore


class firebase_config:
    def __init__(self):
        cred = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()


    def login_control(self, username, password):
        doc_ref = self.db.collection('Hasta').document(username)
        doc = doc_ref.get()
        app = firebase_admin.get_app(name='[DEFAULT]')
        firebase_admin.delete_app(app)
        if doc.exists:
            doc = doc_ref.get()
            user_data = doc.to_dict()
            db_password = user_data['password']
            if password == db_password:
                return True
            else:
                return False

        else:
            return False