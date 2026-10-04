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

## Pendiente

Unir esta parte con los módulos de mis compañeros en el menú principal y agregar los cambios que se pidan en los sprints. Al integrar el README, hay que conservar las bitácoras de todos.