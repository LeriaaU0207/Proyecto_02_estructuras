# Proyecto 2 - Estructuras de Datos

Sistema de archivos distribuido y enrutador de red.

## Mi parte - Boris Arias Quintana

Me corresponde la parte C: el grafo y el enrutamiento de los servidores.

Esta parte permite agregar y eliminar servidores y conexiones. Usa Dijkstra para buscar la ruta de menor latencia y mostrar los saltos y el costo total. También usa BFS para hacer un ping general y revisar cuáles servidores son alcanzables y cuáles están aislados.

Las operaciones se guardan en `network_audit_log.txt`. El menú tiene una opción para ver esos registros.

## Archivos

- `grafo.py`: guarda las conexiones e implementa Dijkstra y BFS.
- `network_manager.py`: maneja las operaciones de red y la auditoría.
- `menu_red.py`: permite probar mi parte desde un menú.
- `pruebas_red.py`: comprueba las rutas y otros casos del módulo.

Para abrir el programa se ejecuta `menu_red.py`. La opción 9 carga un ejemplo para probarlo.

## Bitácora de IA

**3 de octubre de 2026 - ChatGPT/Codex**

Le pasé el PDF del proyecto, la división del trabajo y el código de mis compañeros. Pedí ayuda para generar mi parte completa siguiendo los requisitos, con código sencillo y comentarios cortos.

Una parte de lo que pedí fue: “Hazlo lo mas estudiante novato posible. Pero obvio siguiendo todos los pasos y con un perfil muy bueno”.

La IA generó los archivos del módulo y las pruebas. Después pedí simplificarlo porque algunas partes estaban más elaboradas de lo que quería: “Porfa se que tiene que ser elaborado pero no tanto”.

Se simplificaron algunas condiciones y las pruebas, manteniendo Dijkstra, BFS y la auditoría. Reemplacé los archivos anteriores e hice el commit en mi rama Boris.

**7 de octubre 2026

Uni todas las partes con los módulos de mis compañeros en el menú principal y agregar los cambios que se pidan en los sprints. Al integrar el README, hay que conservar las bitácoras de todos.
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
Herramienta de IA utilizada: ChatGPT (GPT-6 Sol Light) y DeepSeek 
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
- «Te envío el proyecto a como lo tenemos montado como grupo, ya cumple con los requerimientos de la rúbrica del profesor?». --> Se revisó el código y se encontraron algunas correcciones que se realizaron, también hacía falta hacerle más pruebas para comprobar que el programa funcionaba correctamente.Faltba la integraación de los módulos en el menú principal, sistema por servidor, autenticación y auditoría en el file_system_manager.py. También se arreglaron bugs dentro de la función mostrar_arbol
- «Ya quedaron los cambios implementados y ya este seria de as ultimas versiones del proyecto?» --> Se revisó el código y se encontraron algunas correcciones que se realizaron, también hacía falta hacerle más pruebas para comprobar que el programa funcionaba correctamente.
- «¿Cómo podría implementar la parte de persistencia a los servidores?? o las indicacaiones sugieren que sean sin eso?» --> Como tal en la rubrica el unico requisito era como tal el registro de la auditoria y usuarios. 

Nota: Todo el código que haya sido generado por la IA fue probado y adaptado antes de incorporarlo al proyecto
---

- Semana 0: Se hizo la organización base del equipo y se repartó el trabajo en grupos. También se hizo la lectura de los requisitos y la definición de la estructura en la que se desarrollará el proyecto.

- 27/09/2026 --> Valeria: Se crea la clase Nodo y se definen los métodos de búsqueda y creación de nodos. Se crea el archivo file_system_manager.py y se completa la clase FileSystemManager. Se completa la función main.py como un temporal para probar la estructura y se elimina despues. También se crea la bitácora de IA que se utilizó para el proyecto.

- 03/10/2026 --> Se realiza el merge hacia la rama de main para probar el proyecto en su estado final.

- 07/10/2026 --> Se realizaron unas correcciones sobre las validaciones al proyecto y se realizaron las primeras pruebas con las implementaciones realizadas, con el fin de encontrar errores y corregirlos.

- 09/10/2026 --> Se realizaron las pruebas para el funcionamiento del código en general 

## Sprints semanales

Durante el período de desarrollo del proyecto no se publicaron sprints
adicionales en la plataforma de la U o mencionados en clase.
Se revisó periódicamente la plataforma y el único material publicado fueron las preguntas para la defensa técnica del proyecto.
Por lo tanto, no hubo requerimientos semanales que integrar. El proyecto se desarrolló con base en los requerimientos originales del PDF y las preguntas de defensa publicadas al final.