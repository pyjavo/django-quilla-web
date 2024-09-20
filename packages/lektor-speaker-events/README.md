# Speaker Events

Este plugin adiciona un nuevo filtro llamado `speakerevent` en jinja que permite filtrar los eventos por usuario
para ello se requiere que los eventos tengan la siguiente estructura

Recibe de parametro un listado de eventos, que se obtiene del tipo de datos Query de lektor
que se obtiene de la siguiente manera:

```python
site.query('/eventos', alt)
```

Este modelo debe tener un campo talks de tipo flow el cual contiene en su modelo los siguientes campos:

speaker
title
