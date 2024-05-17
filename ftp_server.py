from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    #Crea un autorizador que se encarga de la autorizacion y verificacion de los usuarios 
    authorizer = DummyAuthorizer()
    
    #Añade un usuario con nombre de usuario, contraseña, directorio al que accedera cuando se conecte y con permisos de lectura y escritura
    #Tambien se le puede personalizar el mensaje que se muestra cuando el usuario se conecta y desconecta
    authorizer.add_user("user", "12345", "/Users/valen/FTP-FTPS_implementacion/user", perm="elradfmw", msg_login="Conexión exitosa", msg_quit="Te has desconectado")
    #"e" = Autoriza cambiar de carpeta
    #"l" = Autoriza listar archivos
    #"r" = Autoriza descargar archivos del servidor
    #"a" = Autoriza agregar data a un archivo existente
    #"d" = Autoriza a eliminar un archivo o carpeta
    #"f" = Autoriza a renombrar un archivo o carpeta
    #"m" = Autoriza crear carpetas
    #"w" = Autoriza subir archivos al servidor
    
    #Añade un usuario anonimo con permisos de lectura unicamente y el directorio al que accedera cuando se conecte
    authorizer.add_anonymous("/Users/valen/FTP-FTPS_implementacion/anonimo", msg_login="Conexión exitosa", msg_quit="Te has desconectado")

    #Se crea el handler que se encarga de manejar los comandos y las operaciones del server
    handler = FTPHandler
    #Se le asigna el autorizador al handler porque es un requerimiento para que funcione
    handler.authorizer = authorizer

    #Crea el servidor en la direccion ip y puerto especificado
    server = FTPServer(("0.0.0.0", 21), handler)

    #Levanta el servidor 
    server.serve_forever()

if __name__ == "__main__":
    main()
