# Cornershop Test

## Corneshop-Backend

### **Prerequisitos**

Es necesario crear en la raiz del proyecto un archivo (.env)
y agregar toda la informacion del .env.false ademas de crear un token 
de slack donde se realizaran las notificaciones.

    SLACK_TOKEN=xoxb-2407190307699-2407267970371 # ejemplo de token
    SLACK_CHANNEL=backend-developer  # ejemplo de canal

#### **Creación y activación del entorno via docker**

1.- instalar docker [DOCKER](https://docs.docker.com/docker-for-windows/install/)

2.- ir a la carpeta cornershop-backend
    
    cd cornershop-backend

3.- crear el archivo de configuración

    touch .env
    
copiar la informacion del archivo .env.false

4.- Ejecutar el comando:

    docker-compose build

5.- Ejecutar el comando para levantar el entorno

    docker-compose up
        
6.- url del backend

    http://127.0.0.1:8000

* Nota.

    las documentación de los servicios se encuenta en la carpeta docs 

6.- Usuarios para llamada de servicios.

Actualmente se realizo la migracion de 2 usuarios al momento de iniciar el proyecto
* usuario administrador.
    
        username=nora
        password=1234qwer*
* usuario empleado.

        username=test
        password=Test1234*

para realizar las pruebas
     
## Corneshop-frontend
#### **Creación y activación del entorno via docker**

1.- instalar docker [DOCKER](https://docs.docker.com/docker-for-windows/install/)

2.- ir a la carpeta cornershop-frontend
    
    cd cornershop-frontend
 
3.- Ejecutar el comando:

    docker-compose build

4.- Ejecutar el comando para levantar el entorno

    docker-compose up

5.- url para entrar

    http://127.0.0.1:3000
