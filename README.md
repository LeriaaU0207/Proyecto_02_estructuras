# Proyecto_02_estructuras
### Adaptación y revisión

La IA se utilizó como una herramienta de apoyo y guía durante el desarrollo, pero el código no fue simplemente copiado y utilizado directamente.

El desarrollo se realizó poco a poco. Mientras ChatGPT explicaba y proponía cada parte del código, yo la iba escribiendo manualmente en Visual Studio Code y tratando de comprender qué hacía cada línea antes de continuar con la siguiente parte.

Durante este proceso también se presentaron distintos errores, principalmente relacionados con nombres de clases, métodos, importaciones e indentación. Estos errores se fueron revisando y corrigiendo uno por uno mediante la ejecución y prueba del programa.

Una vez terminadas las clases, se realizaron pruebas para verificar:

- Registro de usuarios.
- Rechazo de usuarios duplicados.
- Inicio de sesión con contraseña correcta e incorrecta.
- Búsqueda y eliminación de usuarios.
- Funcionamiento de la función Hash.
- Manejo de colisiones mediante encadenamiento.
- Registro de las acciones en `network_audit_log.txt`.

También se realizó una prueba específica para encontrar automáticamente dos nombres de usuario que generaran el mismo índice Hash. Esto permitió comprobar que varios usuarios podían permanecer almacenados en una misma posición mediante el encadenamiento sin perder información.

El objetivo de trabajar de esta manera fue ir comprendiendo progresivamente el código desarrollado y no solamente obtener un programa funcional, especialmente porque cada integrante debe poder explicar y defender técnicamente su módulo.
/ Network OS — Proyecto 2 EIF207
Simulación de un sistema de archivos distribuido y enrutador de red.

## Estructura del proyecto
Repositorio de GitHub: https://github.com/LeriaaU0207/Proyecto_02_estructuras.git

## Bitácora de Inteligencia Artificial
---
Valeria Bahena Mújica - Persona A. Responsable de los árboles de directorios.
Herramienta de IA utilizada: ChatGPT (GPT-6 Sol Light)
Módulos creados: 
- file_system_manager.py: Clase que representa un árbol de directorios.
- nodo.py: Clase que representa un nodo de un árbol de directorios.
- pruebas_arbol.py: Script que realiza pruebas de la clase FileSystemManager.

Consultas realizadas:
- "Ayúdame con un paso a paso para desarrollar la parte de árboles de directorios del proyecto en Python" --> Se utilizó para planificar las clases Nodo y FileSystemManager, la raíz /, las operaciones del árbol y su integración futura con un sistema de archivos por servidor.
- "¿Voy por buen camino con mi código de nodo.py y file_system_manager.py?" --> Se revisó el código inicial. A partir de la explicación, se distinguió la búsqueda por ruta de la búsqueda recursiva por nombre y se corrigió la eliminación para usar el padre real del nodo.
- «VS Code marca un problema en nombre += "/"; ¿esa sintaxis existe en Python?». --> Se aclaró que += es válido en Python y se revisó el método que muestra el árbol con indentación.
- «Tengo un error en _limpiar_subarbol; ¿cómo lo corrijo?». --> Se identificó que nodo.hijos.clear = [] debía escribirse nodo.hijos.clear(). Se ejecutó nuevamente el programa para comprobar la corrección.
- «¿Dónde coloco los try/except para que las pruebas inválidas no detengan el programa?». --> Se colocaron en el archivo de pruebas, alrededor de cada operación que debía fallar. Se verificaron nombres repetidos, creación dentro de un archivo y rutas inválidas.
- «Genera pruebas para eliminar un archivo, borrar una carpeta en cascada, proteger la raíz y rechazar una ruta inexistente». --> Se prepararon escenarios independientes para comprobar el comportamiento del módulo. Actualizar esta fila con los resultados de las pruebas que efectivamente se hayan ejecutado.

Nota: Todo el código fue probado y adaptado antes de incorporarlo al proyecto
---

- Semana 0: Se hizo la organización base del equipo y se repartó el trabajo en grupos. También se hizo la lectura de los requisitos y la definición de la estructura en la que se desarrollará el proyecto.
- Semana 1: 
27/09/2026 --> Valeria: Se crea la clase Nodo y se definen los métodos de búsqueda y creación de nodos. Se crea el archivo file_system_manager.py y se completa la clase FileSystemManager. Se completa la función main.py como un temporal para probar la estructura y se elimina despues. También se crea la bitácora de IA que se utilizó para el proyecto.


## Sprints semanales (Implementaciones que decide agregar el profesor al proyecto)
- 
