# Carpetas
Música/
├── Rock/
│   ├── Album 1/
│   │   ├── canción 1.mp3
│   │   └── canción 2.mp3
│   └── Album 2/
│
├── Electrónica/
│   └── ...
│
└── Música mexicana/
    └── ...

# Estructura del proyecto
mi_reproductor/
│
├── main.py
│
├── app/
│   ├── __init__.py
│   ├── ventana.py
│   ├── biblioteca.py
│   ├── reproductor.py
│   ├── base_datos.py
│   └── configuracion.py
│
├── ui/
│   ├── biblioteca.ui
│   └── estilos.css
│
├── data/
│   └── musica.db
│
└── recursos/
    ├── iconos/
    └── portada_default.png

# Primera versión
No intentaría hacer todo de golpe.
## Versión 0.1
    Ventana GTK4.
    Botón para seleccionar carpeta.
    Leer carpeta Música.
    Encontrar MP3/FLAC/OGG/WAV.
    Mostrar las canciones.
    Reproducir.
    Pausar.
    Detener.
    Siguiente/anterior.
    Control de volumen.

## Versión 0.2
    Artista.
    Álbum.
    Género.
    Duración.
    Portadas.
    Buscador.
    Ordenar canciones.

## Versión 0.3
    Favoritos.
    Playlists.
    Historial.
    Reanudar última canción.
    Cola de reproducción.

## Versión 1.0
    Icono de aplicación.
    .desktop.
    Instalación en Fedora.
    Ejecutable/paquete.
    Integración con controles multimedia del escritorio.
    Notificaciones.
    Atajos de teclado.
    Reproducción en segundo plano.