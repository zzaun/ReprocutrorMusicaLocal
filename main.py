import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from app.ventana import Ventana


def main():
    app = Gtk.Application(
        application_id="com.mimusica.Player"
    )

    app.connect("activate", lambda app: Ventana(app))

    app.run()


if __name__ == "__main__":
    main()