import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from datetime import datetime, timedelta
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

        # Etiqueta de bienvenida
        self.welcome_label = Label(text="Welcome to the Taximeter App!", font_size=24)
        self.layout.add_widget(self.welcome_label)

        # Contador de tiempo
        self.time_label = Label(text="Time: 00:00:00", font_size=18)
        self.layout.add_widget(self.time_label)

        # Estado del taxi
        self.status_label = Label(text="Taxi Stopped", font_size=18)
        self.layout.add_widget(self.status_label)

        # Botón para iniciar/detener el taxi
        self.toggle_button = Button(text="Start/Stop", font_size=18)
        self.toggle_button.bind(on_press=self.toggle_movement)
        self.layout.add_widget(self.toggle_button)

        # Selección de factor de demanda
        self.demand_toggle = ToggleButton(text="Auto Demand", group="demand", state="down")
        self.demand_toggle.bind(on_press=self.toggle_demand)
        self.layout.add_widget(self.demand_toggle)

        self.manual_demand_input = TextInput(hint_text="Enter manual demand factor", multiline=False)
        self.layout.add_widget(self.manual_demand_input)

        # Botón para calcular el costo
        self.calculate_button = Button(text="Calculate Cost", font_size=18, disabled=True)
        self.calculate_button.bind(on_press=self.calculate_cost)
        self.layout.add_widget(self.calculate_button)

        # Etiqueta para mostrar el costo
        self.cost_label = Label(text="", font_size=18)
        self.layout.add_widget(self.cost_label)

        # Iniciar el contador de tiempo
        self.start_time = datetime.now()
        Clock.schedule_interval(self.update_time, 1)

        logging.info("GUI initialized.")
        return self.layout

    def toggle_movement(self, instance):
        """
        Cambia el estado del taxi (en movimiento o detenido).
        """
        self.taximeter.toggle_movement()
        new_label = "Taxi Moving" if self.taximeter.taxi_moving else "Taxi Stopped"
        self.status_label.text = new_label
        self.calculate_button.disabled = self.taximeter.taxi_moving  # Deshabilitar cálculo si el taxi está en movimiento
        logging.info(f"Taxi is now {new_label}.")

    def toggle_demand(self, instance):
        """
        Cambia entre factor de demanda automático y manual.
        """
        if self.demand_toggle.state == "down":
            self.taximeter.billing.demand_factor = self.taximeter.billing.auto_demand_factor()
            logging.info(f"Demand factor set to automatic: {self.taximeter.billing.demand_factor}")
        else:
            try:
                demand_factor = float(self.manual_demand_input.text)
                self.taximeter.billing.demand_factor = demand_factor
                logging.info(f"Demand factor set to manual: {self.taximeter.billing.demand_factor}")
            except ValueError:
                logging.warning("Invalid manual demand factor entered.")

    def calculate_cost(self, instance):
        """
        Calcula el costo del viaje y lo muestra en la interfaz.
        """
        if not self.taximeter.taxi_moving:
            cost = self.taximeter.calculate_trip_cost()
            cost_without_vat = cost / (1 + self.taximeter.billing.VAT_RATE)
            self.cost_label.text = f"Cost (without VAT): {cost_without_vat:.2f} €\nCost (with VAT): {cost:.2f} €"
            logging.info(f"Trip cost calculated: {cost:.2f}€")
        else:
            self.cost_label.text = "Cannot calculate cost while taxi is moving."

    def update_time(self, dt):
        """
        Actualiza el contador de tiempo.
        """
        elapsed_time = datetime.now() - self.start_time
        self.time_label.text = f"Time: {str(elapsed_time).split('.')[0]}"
        self.taximeter.update_time(1)  # Actualiza el tiempo en el taxímetro cada segundo

if __name__ == "__main__":
    logging.info("Application started.")

    # Verifica la autenticación
    if Authentication.login():
        # Inicia la aplicación Kivy
        TaximeterApp().run()

    logging.info("Application closed.")