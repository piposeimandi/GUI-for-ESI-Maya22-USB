#!/bin/bash

# Crear estructura de directorios para el paquete
PACKAGE_NAME="maya22_package"
INSTALL_DIR="$PACKAGE_NAME/usr/share/maya22-panel-control"

# Limpiar la estructura anterior si existe
rm -rf $PACKAGE_NAME
mkdir -p $INSTALL_DIR
mkdir -p $PACKAGE_NAME/DEBIAN

# Copiar archivos fuente al directorio de instalación del paquete
cp -r src/* $INSTALL_DIR/

# Copiar los archivos de control y postinst al directorio DEBIAN
cp debian/control $PACKAGE_NAME/DEBIAN/
cp debian/postinst $PACKAGE_NAME/DEBIAN/
cp debian/maya22.desktop $INSTALL_DIR/
cp debian/icono.png $INSTALL_DIR/

chmod +x $PACKAGE_NAME/DEBIAN/postinst

# Construir el paquete .deb
dpkg-deb --build $PACKAGE_NAME
