import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class Ventana(Gtk.ApplicationWindow):

    def __init__(self, app):
        super().__init__(
            application=app,
            title="Mi Música"
        )

        self.set_default_size(900, 600)

        self.crear_interfaz()

        # Mostrar la ventana
        self.present()

    def crear_interfaz(self):

        caja = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        caja.set_margin_top(20)
        caja.set_margin_bottom(20)
        caja.set_margin_start(20)
        caja.set_margin_end(20)

        titulo = Gtk.Label(
            label="Mi Música"
        )

        caja.append(titulo)

        self.set_child(caja)