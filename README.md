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

puede instalar imagemagick usando chocolatey, o descargar desde el siguiente enlace:

<http://www.imagemagick.org/>

Para instalar lektor puede usar el siguiente comando:

```powershell
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))" && SET PATH=%PATH%;%LocalAppData%\lektor-cli
```

Pero tambien puede ser ejecutado directamente en powershell:

```powershell
    iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))
```

### Linux

En ubuntu se pueden instalar las dependencias de lektor usando el comando:

    sudo apt-get install python-dev libssl-dev libffi-dev imagemagick

Luego puede instalar lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/install.sh | sh

### MacOS

En Mac OS si se tiene instalado homebrew se pueden instalar las dependencias de lektor usando el comando:

    brew install imagemagick

Luego puede instalar lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/install.sh | sh

## Ejecución del proyecto durante desarrollo

Para la ejecución del proyecto se debe ejecutar el comando

```bash
lektor server -f webpack
```

## Producción

Construye el proyecto en los artefactos finales

```bash
lektor build -f webpack
```

## Código de conducta

Los invitamos a leer el siguiente [repositorio con el código de conducta](https://github.com/PyBAQ/codigo-de-conducta) de la comunidad.

### Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

[CONTRIBUTING.md]: https://github.com/PyBAQ/django-quilla-web/blob/master/CONTRIBUTING.md
