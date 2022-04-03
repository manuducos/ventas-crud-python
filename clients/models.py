import uuid

class Client():
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()
    
    def to_dict(self):
        return vars(self)
    
    @staticmethod # Permite generar metodos estaticos que se pueden ejecutar sin necesidad de una instancia de clase
    def schema(): # No recibe el keyword self porque no necesita una instancia
        return ['name', 'company', 'email', 'position', 'uid']