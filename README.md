# Página web comunidad python barranquilla

[![Build Status](https://travis-ci.org/PyBAQ/django-quilla-web.svg?branch=master)](https://travis-ci.org/PyBAQ/django-quilla-web)

## Instalación

Para poder ejecutar el proyecto localmente se requieren las siguientes dependencias:

- Python 2.7
- Imagemagick
- NodeJS 6
- [Lektor](https://www.getlektor.com/)

A continuación siga la guiá de instalación según su sistema operativo

### Windows

Para windows puede descargar python desde el siguiente enlace: https://www.python.org/downloads/

puede instalar imagemagick usando [chocolatey](https://chocolatey.org/), o descargar desde el siguiente enlace:

<http://www.imagemagick.org/>

Para instalar lektor puede usar el siguiente comando:

```powershell
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))" && SET PATH=%PATH%;%LocalAppData%\lektor-cli
```

Pero tambien puede ser ejecutado directamente en powershell:

```powershell
    iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))
```

### Windows 10: Windows Subsystem for Linux

Si quieres/debes mantener windows instalado, pero prefieres mantener este proyecto en linux, puedes usar el "Windows Subsystem for Linux" (subsistema de windows para linux).  La forma rápida de habilitarlo es por powershell en modo de Administrador, ten presente que necesitas reinicar tu PC:

```powershell
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Luego, en la tienda de microsoft encontrarás distintas distribuciones de ubuntu que podrás instalar, ten presente que esto solo te da acceso por linea de comandos. Podrás encontrar mas detalles en el siguiente vínculo: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

De allí continua los pasos según el instructivo para Linux.

### Linux

En ubuntu se pueden instalar las dependencias de lektor usando el comando:

    sudo apt-get install python-dev libssl-dev libffi-dev imagemagick

Luego puede instalar lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/install.sh | sh

### MacOS

En Mac OS si se tiene instalado [homebrew](https://brew.sh/) se pueden instalar las dependencias de lektor usando el comando:

    brew install imagemagick

Luego puede instalar lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/install.sh | sh

Verificar que las variables de entorno del formato UTF-8 en sus respectivos idiomas esten definidas en el
archivo ~/.bash_profile de su sistema y en caso de no estar definidas agregarlas.

```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Docker

Si tienes Docker instalado (https://docs.docker.com/install/) puedes hacer uso del Dockerfile en el directorio principal para crear una imagen y posteriormente ejectar un contenedor con todas las dependencias necesarias. Desde el directorio principal del repositorio ejecuta:

```bash
# Bash o Powershell
docker build -t pybaq .
docker run --rm -p 5000:5000 -v ${PWD}:/app --name pybaq-local pybaq

# Windows Command Line
docker build -t pybaq .
docker run --rm -p 5000:5000 -v %cd%:/app --name pybaq-local pybaq
```

Al montar la carpeta con el codigo fuente (`-v ${PWD}:/app` o `-v %cd%:/app`) los cambios que se hagan al codigo se propagaran al contenedor y se veran reflejados immediatamente.

**Nota:** Verifica que el directorio donde tienes el codigo fuente puede ser montado como un Docker volume. En Linux no se requiere configuración extra, pero hay diferentes metodos para [MacOS](https://docs.docker.com/docker-for-mac/#file-sharing) y [Windows](https://blogs.msdn.microsoft.com/wael-kdouh/2017/06/26/enabling-drive-sharing-with-docker-for-windows/) dependiendo del modo de instalación.

### La discusión Python3

Ahora mismo Lektor **no provee** una forma confiable y sencilla de instalar la herramienta en Linux usando Python 3. Por esto no usamos esta versión de Python. Sin embargo todos los pasos anteriormente descritos en windows funcionan sin inconvenientes usando cualquier versión de Python 3.6+. Será, sin embargo, tu responsabilidad inspeccionar el código fuente de los plugins de Lektor para segurar su compatibilidad con Python 3. Recuerda que es codigo libre y no se trata de pedir las cosas sino de contribuir a las características que deseas.


## Ejecución del proyecto durante desarrollo

Para la ejecución del proyecto se debe ejecutar el comando:

```bash
lektor server
```

Al ejecutar lektor, verás una lista de procesos que tienen lugar antes de generar la página estática. Si en tu edición cometes algún error, aparecerá escrito en la consola. Si se genera con exito la página, ésta estará disponible en [http://localhost:5000/](http://localhost:5000/).

## Código de conducta

Los invitamos a leer el siguiente [repositorio con el código de conducta](https://github.com/PyBAQ/codigo-de-conducta) de la comunidad.

### Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

[CONTRIBUTING.md]: https://github.com/PyBAQ/django-quilla-web/blob/master/CONTRIBUTING.md

## Actualizar eventos

En un terminal bash ejecuta el siguientes script python (debes instalar el paquete requests con pip)

```bash
python scripts/events.py
```

> por favor actualiza los eventos solo si lo consideras estrictamente necesario, entre los metadatos incluidos incluye la fecha de actualización en un timestamp (propenso a conflictos)

## Validar html usando w3c validator

Hay un paquete que usa los servicios de w3c para validar [HTML](https://validator.w3.org/) y [CSS](https://jigsaw.w3.org/css-validator/)

puedes instalarlo usando el comando
```
pip install -U Online-W3C-Validator
```

luego para verificar los contenidos 
```
lektor build --output-path ./build
cd build
w3c_validator $(find . -type f -name \*.html)
```

## Compilar css

El proyecto actualmente usa sass para los estilos en cascada si deseas modificarlos es necesario que tengas instalado nodeJS

para instalar con npm las dependencias ejecuta

```
npm install
```

Luego cada vez que actualices un estilo ejecuta
```
npm build
```
