
from flask import Flask
from flask_restx import Api, Resource
from src.server.instance import server
from src.models.konsi import *
import requests
import json
from time import sleep, perf_counter
from threading import Thread

app, api = server.app, server.api

consulta = [{}]
payload = {"login":"","senha":"",}

threads = []

def task(cpf,config,header_consulta):
            beneficios=[]                  
            response = requests.get(
                    config["host"]+config["consulta"]+cpf,
                    headers=header_consulta,
                    verify=False,
                )
            data = json.loads(response.content.decode()) 
            for i in range(len(data["beneficios"])):  
                 beneficios.append(data["beneficios"][i]["nb"])
            consulta.append(result(cpf,beneficios))
            resultado =  result(cpf,beneficios)
            print(resultado)

@api.route('/konsi')
class Konsi(Resource):

    @api.expect(input,validate=True)
    @api.marshal_list_with(consulta_model)
    #@api.marshal_list_with(mode)
    def get(self,):
        with requests.session() as sess:
            with open("src/configuracao/konsi.json") as file:
               config = json.loads(file.read())
            
            json_in = api.payload
            payload["login"] = json_in["login"]
            payload["senha"] = json_in["senha"]

            response = sess.get(
                config["url"], 
                headers=config["header_site"],
                verify=False,
                )
            
            response = sess.options(
                config["host"]+config["login"],
                headers=config["header_login_options"],
                verify=False,
            )   

            response = sess.post(
                config["host"]+config["login"],
                headers=config["header_login_post"],
                json=payload,
                verify=False,
            )
                      
            if response.status_code == 200: 
                header_logado = config["header_logado"]
                header_consulta = config["header_consulta"]
                header_logado["Authorization"] = response.headers["Authorization"]
                header_consulta["Authorization"] = response.headers["Authorization"]
                response = requests.get(
                    config["host"]+config["logado"],
                    headers=config["header_logado"],
                    verify=False,
                    data = payload
                )
                for cpf in json_in["cpf"]:    
                    t = Thread(target=task, args=(cpf,config,header_consulta))
                    threads.append(t)
                    t.start()

                for t in threads:
                    t.join()

            else:
                return response.status_code
        return consulta
    

