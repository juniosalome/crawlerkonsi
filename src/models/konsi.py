from flask_restx import fields
from src.server.instance import server
import json

input = server.api.model('Input', {
    'login' : fields.String(required=True,min_length=1, max_length=200,description='Usuário cadastrado.'),
    'senha' : fields.String(required=True, min_length=1, max_length=200, description='Senha cadastrada'),
    'cpf': fields.List(fields.String(),required=True, description='Array de CPFs dos clientes que iremos consultar', ),
})

consulta_model = server.api.model('consulta_model', {
    'cpf' : fields.String(required=True,min_length=1, max_length=200,description='CPF consultado.'),
    'beneficio' : fields.List(fields.String(), required=True,  description='Benefício encontrado',),
})

mode = server.api.model('mode',{})

class result:
    def __init__(self, cpf, beneficio):
        self.beneficio = []
        self.cpf = cpf 
        self.beneficio = beneficio
    def __str__(self):
        return (str(self.cpf ) + str(self.beneficio) )


