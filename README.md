# Página Web comunidad Python Barranquilla

[![Build Status](https://travis-ci.org/PyBAQ/django-quilla-web.svg?branch=master)](https://travis-ci.org/PyBAQ/django-quilla-web)

## Instalación

Primero haz un Fork del proyecto en GitHub y luego clonalo en tu computador así:

  SSH: git clone git@github.com:PyBAQ/django-quilla-web.git

  HTTPS: git clone https://github.com/PyBAQ/django-quilla-web.git

Para poder ejecutar el proyecto localmente se requieren las siguientes dependencias:

- Python 3
- ImageMagick
- [Lektor](https://www.getlektor.com/docs/installation/)

A continuación siga la guía de instalación según su sistema operativo

### Windows

Para Windows puedes descargar Python desde el siguiente enlace: https://www.python.org/downloads/windows/

Puedes instalar ImageMagick desde el siguiente enlace: <https://imagemagick.org/>

o usar [chocolatey](https://chocolatey.org/) y ejecutar

    choco install imagemagick

Para instalar Lektor puedes usar el siguiente comando:

```powershell
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))" && SET PATH=%PATH%;%LocalAppData%\lektor-cli
```

Pero también puede ser ejecutado directamente en powershell:

```powershell
    iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))
```

### Windows 10: Windows Subsystem for Linux

Si quieres/debes mantener Windows instalado, pero prefieres mantener este proyecto en Linux, puedes usar el "Windows Subsystem for Linux" (subsistema de Windows para Linux).  La forma rápida de habilitarlo es por powershell en modo de Administrador, ten presente que necesitas reinicar tu PC:

```powershell
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Luego, en la tienda de Microsoft encontrarás distintas distribuciones de Ubuntu que podrás instalar, ten presente que esto solo te da acceso por linea de comandos. Podrás encontrar mas detalles en el siguiente vínculo: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

De allí continua los pasos según el instructivo para Linux.

### Linux

En Ubuntu se pueden instalar las dependencias de Lektor usando el comando:

    sudo apt install python3-dev libssl-dev libffi-dev imagemagick

Luego puedes instalar Lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/installer.py | python3

### MacOS

En Mac OS si se tiene instalado [homebrew](https://brew.sh/) se pueden instalar las dependencias de Lektor usando el comando:

    brew install imagemagick

Luego puede instalar Lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/installer.py | python3

Verificar que las variables de entorno del formato UTF-8 en sus respectivos idiomas esten definidas en el
archivo ~/.bash_profile de su sistema y en caso de no estar definidas agregarlas.

```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Docker

Si tienes Docker instalado (https://docs.docker.com/get-docker/) puedes hacer uso del Dockerfile en el directorio principal para crear una imagen y posteriormente ejecutar un contenedor con todas las dependencias necesarias. Desde el directorio principal del repositorio ejecuta:

```bash
# Bash o Powershell
docker build -t pybaq . # Tener presente el "."
docker run --rm -p 5000:5000 -v ${PWD}:/app --name pybaq-local pybaq

# Windows Command Line
docker build -t pybaq . # Tener presente el "."
docker run --rm -p 5000:5000 -v %cd%:/app --name pybaq-local pybaq
```

Al montar la carpeta con el código fuente (`-v ${PWD}:/app` o `-v %cd%:/app`) los cambios que se hagan al código se propagaran al contenedor y se veran reflejados immediatamente.

**Nota:** Verifica que el directorio donde tienes el código fuente puede ser montado como un Docker volume. En Linux no se requiere configuración extra, pero hay diferentes métodos para [MacOS](https://docs.docker.com/docker-for-mac/#file-sharing) y [Windows](https://blogs.msdn.microsoft.com/wael-kdouh/2017/06/26/enabling-drive-sharing-with-docker-for-windows/) dependiendo del modo de instalación.


## Ejecución del proyecto durante desarrollo

Para la ejecución del proyecto se debe ejecutar el comando:

```bash
lektor server
```

Al ejecutar Lektor, verás una lista de procesos que tienen lugar antes de generar la página estática. Si en tu edición cometes algún error, aparecerá escrito en la consola. Si se genera con éxito la página, ésta estará disponible en [http://localhost:5000/](http://localhost:5000/).

## Código de conducta

Los invitamos a leer el siguiente [repositorio con el código de conducta](https://github.com/PyBAQ/codigo-de-conducta) de la comunidad.

### Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

[CONTRIBUTING.md]: https://github.com/PyBAQ/django-quilla-web/blob/master/CONTRIBUTING.md

## Actualizar eventos

En un terminal bash ejecuta el siguiente script Python (debes instalar el paquete requests con pip)

```bash
python scripts/events.py
```

Se genera el archivo databags/meetup.json con los eventos actualizados. Recuerda adicionarlo al Pull Request con un commit.

> Por favor actualiza los eventos solo si lo consideras estrictamente necesario, entre los metadatos incluidos incluye la fecha de actualización en un timestamp (propenso a conflictos)

## Validar HTML usando W3C validator

Hay un paquete que usa los servicios de W3C para validar [HTML](https://validator.w3.org/) y [CSS](https://jigsaw.w3.org/css-validator/)

puedes instalarlo usando el comando:
```
pip install -U Online-W3C-Validator
```

luego para verificar los contenidos:
```
lektor build --output-path ./build
cd build
w3c_validator $(find . -type f -name \*.html)
```

## Compilar CSS

El proyecto actualmente usa Sass para los estilos en cascada si deseas modificarlos es necesario que tengas instalado Node.js.

para instalar con npm las dependencias ejecuta:

```
npm install
```

Luego cada vez que actualices un estilo ejecuta:
```
npm build
```
