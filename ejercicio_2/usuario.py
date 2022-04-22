import json
import os

class usuario():
    def __init__(self,\
                 nombre,\
                 apellidos,\
                 edad,\
                 email):
        self.info = {
                    "Nombre" : nombre,
                    "Apellidos" : apellidos,
                    "edad"  : edad,
                    "email" : email,
                }
    def save_user(self):                        
        filesize = os.path.getsize("usuarios.json") 
        try:       
            if filesize == 0:
                with open("usuarios.json", "w") as f:
                    json.dump([self.info], f, indent=4)
            if filesize != 0:
                data = json.load(open('usuarios.json'))
                if type(data) is dict:
                    data = [data]       
                data.append(self.info)

                with open("usuarios.json", "w") as f:
                    json.dump(data, f, indent=4)
            
            return 0
        except Exception as E:
            print("Ocurrio un error guardando el registro...")
            print(E)
            return 1

    @staticmethod
    def modificar(usuario, nueva_edad, nuevo_email):
        with open("usuarios.json", "r") as f:
            lista_usuarios = json.load(f)
            lista_usuarios_as_json = json.dumps(lista_usuarios)
        usuarios = json.loads(lista_usuarios_as_json)
        posicion = next(pos for pos,registro in enumerate(usuarios) if registro["Nombre"] == usuario)    
        usuario = next(registro for registro in usuarios if registro["Nombre"] == usuario)
        usuario["edad"] = nueva_edad 
        usuario["email"] = nuevo_email
        usuarios[posicion] = usuario
        with open("usuarios.json", "w") as f:
                json.dump(usuarios, f, indent=4)

    @staticmethod
    def eliminar(nombre):
        with open("usuarios.json", "r") as f:
            lista_usuarios = json.load(f)
            lista_usuarios_as_json = json.dumps(lista_usuarios)        
        usuarios = json.loads(lista_usuarios_as_json)
        posicion = next(pos for pos,registro in enumerate(usuarios) if registro["Nombre"] == nombre)
        del usuarios[posicion]
        with open("usuarios.json", "w") as f:
                json.dump(usuarios, f, indent=4)

    @staticmethod
    def get_all_users():
        filesize = os.path.getsize("usuarios.json")
        if filesize != 0:
            with open("usuarios.json", "r") as f:
                lista_usuarios = json.load(f)
                lista_usuarios_as_json = json.dumps(lista_usuarios)
            return json.loads(lista_usuarios_as_json)
        else:
            return 1

    @staticmethod
    def get_user_by_name(nombre):
        with open("usuarios.json", "r") as f:
            lista_usuarios = json.load(f)
            lista_usuarios_as_json = json.dumps(lista_usuarios)
        try:
            usuario = next(registro for registro in json.loads(lista_usuarios_as_json) if registro["Nombre"] == nombre)
            return usuario
        except Exception as e:
            print(e)
            return 1

    def __repr__(self):
        return "Username : {}\n\
                Apellidos : {}\n\
                Edad : {}\n\
                Email : {}".format(self.nombre,\
                                      self.apellidos,\
                                      self.edad,\
                                      self.email)     