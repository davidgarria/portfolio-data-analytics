\# Chuleta de terminal



pwd        -> dónde estoy. 		-> "Print working directory"
ls         -> qué hay aquí. 		-> "List"
cd carpeta -> entrar en una carpeta. 	-> "Change directory - carpeta"
cd ..      -> subir un nivel. 		-> "Change directory - sube un nivel"
mkdir x    -> crear carpeta. 		-> "Make directory - nombre carpeta"

…

\# macOS / Linux: las 5 primeras líneas de un CSV
head -n 5 ventas.csv

\# cuántas filas tiene un CSV
wc -l ventas.csv

\# qué líneas contienen la palabra "Madrid"
grep "Madrid" ventas.csv


\# Git basics	

git init		-> Crea un repositorio nuevo en tu carpeta actual.
git status		-> Muestra el estado actual de tus archivos y cambios.
git add			-> Prepara los archivos modificados para guardarlos.
git commit -m "---"	-> Guarda los cambios preparados de forma oficial en el historial.
git log --oneline	-> Ver historial


\# El ciclo de trabajo diario:

git switch main
git pull                                  # 1. partir de la última versión
git switch -c <nombre-rama-nueva>         # 2. rama para el trabajo nuevo (Crea una rama y nos cambia a ella)
# … trabajamos, editamos archivos …
git status                                # 3. qué ha cambiado
git add .                                 # 4. preparar
git commit -m "Completar práctica 2.1.3"  # 5. guardar la foto
git push -u origin practica-2-1-3         # 6. subir la rama
					  # 7. abrir el pull request en GitHub, revisar y fusionar
					  # 8. volver a main y hacer git pull

\# Para profundizar: 
git diff                       # qué ha cambiado y no está en staging
git diff --staged              # qué está en staging y entrará en el commit
git restore archivo.sql        # descartar cambios no guardados de un archivo
git restore --staged archivo   # sacar un archivo de staging sin perder los cambios
git revert <hash>              # crear un commit que deshace otro commit (forma segura de deshacer un commit ya publicado)
git clone <url> 	       # descarga un repositorio existente con todo su historial.

