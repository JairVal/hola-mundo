#!/bin/bash

# Función para crear carpetas
crear_carpetas() {
  echo "Ingrese el nombre de la carpeta a crear:"
  read carpeta
  mkdir ~/$carpeta
  echo "Carpeta creada con éxito!"
}

# Función para asignar permisos
asignar_permisos() {
  echo "Ingrese el nombre de la carpeta a la que desea asignar permisos:"
  read carpeta
  echo "Ingrese el usuario o grupo al que desea asignar permisos:"
  read usuario
  chown $usuario ~/$carpeta
  echo "Permisos asignados con éxito!"
}

# Función para crear archivos de texto
crear_archivos() {
  echo "Ingrese el nombre de la carpeta en la que desea crear el archivo de texto:"
  read carpeta
  echo "Ingrese el nombre del archivo de texto a crear:"
  read archivo
  touch ~/$carpeta/$archivo.txt
  echo "Archivo de texto creado con éxito!"
}

# Menú de inicio
while true
do
  clear
  echo "Menú de inicio"
  echo "1. Crear carpeta"
  echo "2. Asignar permisos"
  echo "3. Crear archivo de texto"
  echo "4. Salir"
  read -p "Ingrese su opción: " opcion

  case $opcion in
    1) crear_carpetas ;;
    2) asignar_permisos ;;
    3) crear_archivos ;;
    4) exit ;;
    *) echo "Opción inválida. Por favor, ingrese una opción válida." ;;
  esac
done