# TheAllMightys_ISW

Integrantes:
  - Abdel Sandoval - 201573504-2 - abdel.sandoval@sansano.usm.cl
  - Vanessa Guzman - 201573528-k - vanessa.guzman@sansano.usm.cl
  - Alejandro Vilches - 201573554-9 - alejandro.vilches@sansano.usm.cl
 
 Instrucciones de Instalación:
  
  1. Primero que todo necesitamos tener instalado python3
  2. Procedemos a crear un ambiente virtual de python: python -m venv nombre_ambiente
  3. Activamos el ambiente, para esto nos vamos a la carpeta Scrypts que se encuentra dentro del ambiente y realizamos la instruccion: activate.bat
  4. Volvemos a la carpeta general del ambiente (/ambiente) y procedemos a intalar los requerimientos, para esto usamos el comando: 
     pip install -r requirements.txt
  5. Con esto ya podemos comenzar a correr el servidor, asi que ahora nos movemos a la carpeta contenedora del proyecto /TheAllMightys_ISW
  una vez dentro corremos el servidor realizando el comando: python manage.py runserver
  6. Una vez iniciado el servidor, vamos a internet e ingresamos a la Url: localhost:8000/Home
  
 Instrucciones de Uso del Software: 
   La pagina contiene un menu que sera con el cual nos moveremos entre las opciones de la pagina.
   
   Bodega:
   1. Ver Inventario: esta opcion nos permite ver los materiales que existen en la BD y con los cuales se esta trabajando en la pagina
   2. Agregar material: esta opcion nos permite agregar un nuevo material a la BD, para esto completamos todo los campos del formulario con lo que corresponda y damos a guardar. Luego de esto, nos mostrara nuevamente el inventario, confirmando que se ingreso correctamente el material.
   
   Ordenes:
   1. Ver Ordenes: esta opcion nos permite ver las ordenes de materiales existentes en la BD, con su fecha limite correspondiente.
   2. Ordenar Material: esta opcion nos permite crear una nueva orden de material, para esto procedemos a rellenar todos los campos del formulario, teniendo extremo cuidado en el campo de la fecha, ya que si se ingresa un mal formato de fecha la orden no sera agregada y se debera realizar el procedo desde cero. Un buen formato de fecha corresponde a: AAAA-MM-DD.
   
