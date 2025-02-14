import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from taximeter import Taximeter
from authentication import Authentication

# Configuración del logging
logging.basicConfig(filename="taximeter.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class TaximeterApp(App):
    def build(self):
        """
        Construye la interfaz gráfica de la aplicación.
        """
        self.taximeter = Taximeter()
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Etiqueta para mostrar el estado del taxi
        self.status_label = Label(text="Taxi Stopped", font_size=24)
        self.layout.add_widget(self.status_label)

        # Botón para iniciar/detener el taxi
        self.toggle_button = Button(text="Start/Stop", font_size=18)
        self.toggle_button.bind(on_press=self.toggle_movement)
        self.layout.add_widget(self.toggle_button)

        # Botón para calcular el costo
        self.calculate_button = Button(text="Calculate Cost", font_size=18)
        self.calculate_button.bind(on_press=self.calculate_cost)
        self.layout.add_widget(self.calculate_button)

        # Etiqueta para mostrar el costo
        self.cost_label = Label(text="", font_size=18)
        self.layout.add_widget(self.cost_label)

        logging.info("GUI initialized.")
        return self.layout

    def toggle_movement(self, instance):
        """
        Cambia el estado del taxi (en movimiento o detenido).
        """
        self.taximeter.toggle_movement()
        new_label = "Taxi Moving" if self.taximeter.taxi_moving else "Taxi Stopped"
        self.status_label.text = new_label

    def calculate_cost(self, instance):
        """
        Calcula el costo del viaje y lo muestra en la interfaz.
        """
        cost = self.taximeter.calculate_trip_cost()
        self.cost_label.text = f"Total cost: {cost:.2f} €"

if __name__ == "__main__":
    logging.info("Application started.")

    # Verifica la autenticación
    if Authentication.login():
        # Inicia la aplicación Kivy
        TaximeterApp().run()

    logging.info("Application closed.")