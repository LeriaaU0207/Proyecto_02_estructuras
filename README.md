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