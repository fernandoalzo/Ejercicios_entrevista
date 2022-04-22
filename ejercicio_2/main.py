from usuario import usuario
import os
from prettytable import PrettyTable
#import msvcrt
import getch

if __name__ == "__main__":
    
        banner = """       
        ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗          
        ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗         
        ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║         
        ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║         
        ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝██╗██╗██╗
        ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ╚═╝╚═╝╚═╝  
        """
        print(banner)
        while True:
            tabla1 = PrettyTable()
            tabla1.title = 'Lista de Usuarios'
            tabla1.title = 'Lista de Usiarios'
            tabla1.field_names = ["Nombre", "Apellidos", "edad", "email"]
            tabla2 = PrettyTable()
            tabla2.field_names = ["Nombre", "Apellidos", "edad", "email"]
            tabla3 = PrettyTable()
            tabla3.field_names = ["Nombre", "Apellidos", "edad", "email"]
            tabla4 = PrettyTable()
            tabla4.title = 'Eliminar Usuario'
            tabla4.field_names = ["Nombre", "Apellidos", "edad", "email"]
            tabla5 = PrettyTable()
            tabla5.title = 'Datos de usuario'
            tabla5.field_names = ["Nombre", "Apellidos", "edad", "email"]
            print("Seleccione una opcion:")
            print("[1]. listar todos usuarios")
            print("[2]. crear un nuevo registro")
            print("[3]. ver informacion de un usario")
            print("[4]. editar un registro")
            print("[5]. Eliminar un usuario")
            print("------------------------------------")
            print("Escriba cls para limpiar la pantalla")
            print("------------------------------------\n")

            opcion = input("Digite el numero de la opcion => ")
            
            if opcion == "2":
                os.system("cls")
                print("\n\n[2]. crear un nuevo registro")
                nombre = input("Digite el nombre del ususario => ")
                apellidos = input("Digite ls apellidos del ususario => ")
                edad = input("Digite la edad del ususario => ")
                email = input("Digite email del ususario => ")

                if nombre == "" or apellidos == "" or edad == "" or email == "":
                    print("Hay campos vacios...")

                if nombre != "" and apellidos != "" and edad != "" and email != "":
                    nuevo_usuario = usuario(nombre, apellidos, edad, email)
                    estado = nuevo_usuario.save_user()

                    if estado == 0:
                        print("\nSe guardo el registro de forma exitosa...")
                        tabla5.add_row([nombre, apellidos, edad, email])
                        print(tabla5)
                        
                    else:
                        print("Ocurrio un error...")

                print("\n\nPresione una tecla para continuar...\n\n")
                getch()

                
            elif opcion == "cls":
                os.system("cls")    
                print(banner)

            check_contenido_bd = os.path.getsize("usuarios.json")
            if check_contenido_bd == 0:
                print("\nEl archivo de usuarios esta Vacio...")
                print("\n\nPresione una tecla para continuar...\n\n")
                getch()

            elif check_contenido_bd != 0:                   
                if opcion == "1":
                    print("[1]. listar todos usuarios")
                    todos_los_usuarios = usuario.get_all_users()                
                    if todos_los_usuarios == 1:
                        print("\nNo hay registros para mostrar...")
                    elif todos_los_usuarios != 1:  
                        for registro in todos_los_usuarios:                    
                            tabla1.add_row([registro["Nombre"], registro["Apellidos"], registro["edad"], registro["email"]])
                        print(tabla1)
                    print("\n\nPresione una tecla para continuar...\n\n")
                    getch()
                    
                elif opcion == "3":
                    print("[3]. ver informacion de un usario\n")
                    nombre = input("Digite el nombre del ususario => ")
                    tabla5.field_names = ["Nombre", "Apellidos", "edad", "email"]
                    info_usuario = usuario.get_user_by_name(nombre)
                    if info_usuario == 1:
                        print("No existe el registro...")
                    else:
                        tabla5.add_row([info_usuario["Nombre"],\
                                    info_usuario["Apellidos"],\
                                    info_usuario["edad"],\
                                    info_usuario["email"]])
                        print(tabla5)

                    print("\n\nPresione una tecla para continuar...\n\n")
                    getch()
                
                elif opcion == "4":
                    print("[4]. editar un registro\n")
                    nombre = input("Digite el nombre del ususario => ")
                    info_usuario = usuario.get_user_by_name(nombre)
                    if info_usuario == 1:
                        print("No existe el registro...")
                    else: 
                        tabla2.add_row([info_usuario["Nombre"],\
                                    info_usuario["Apellidos"],\
                                    info_usuario["edad"],\
                                    info_usuario["email"]])
                        print(tabla2)

                        nueva_edad = input("Digite la nueva edad del ususario => ")
                        if nueva_edad == "":
                            nueva_edad = info_usuario["edad"]
                        nuevo_email = input("Digite el nuevo correo del ususario => ")
                        if nuevo_email == "":
                            nuevo_email = info_usuario["email"]
                        usuario.modificar(info_usuario["Nombre"],\
                                        nueva_edad,\
                                        nuevo_email)
                        tabla3.add_row([info_usuario["Nombre"],\
                                    info_usuario["Apellidos"],\
                                    nueva_edad,\
                                    nuevo_email])                    
                        print("\nRegistro Actualizado...\n")
                        print(tabla3)
                    print("\n\nPresione una tecla para continuar...\n\n")
                    getch()
                
                elif opcion == "5":
                    print("[5]. Eliminar un usuario")
                    nombre = input("Digite el nombre del ususario => ")
                    info_usuario = usuario.get_user_by_name(nombre)
                    if info_usuario == 1:
                        print("No existe el registro...")
                    else: 
                        tabla4.add_row([info_usuario["Nombre"],\
                                    info_usuario["Apellidos"],\
                                    info_usuario["edad"],\
                                    info_usuario["email"]])
                        print(tabla4)
                        confirmacion = input("¿desea eliminar el registro? [y/n] => ")
                        
                        if confirmacion == "y" or confirmacion == "Y":
                            usuario.eliminar(info_usuario["Nombre"])
                            print("\n Registro Eliminado...")
                        else:
                            print("\n Operacion Cancelada...")
                    print("\n\nPresione una tecla para continuar...\n\n")
                    getch()
                                
                            
            else:
                print("-----------------")
                print("opcion no valida!!!")
                print("-----------------")
                print("\n\nPresione una tecla para continuar...\n\n")
                getch()
                    

