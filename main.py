import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.clock import Clock
from datetime import datetime, timedelta
from taximeter import Taximeter
from authentication import Authentication

# Configuración del logging
logging.basicConfig(filename="taximeter.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class LoginPopup(Popup):
    """
    Ventana emergente para la autenticación.
    """
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.title = "Login"
        self.size_hint = (0.8, 0.4)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True, multiline=False)
        self.layout.add_widget(self.password_input)

        self.login_button = Button(text="Login", size_hint=(1, 0.3))
        self.login_button.bind(on_press=self.attempt_login)
        self.layout.add_widget(self.login_button)

        self.add_widget(self.layout)

    def attempt_login(self, instance):
        """
        Intenta autenticar al usuario.
        """
        username = self.username_input.text
        password = self.password_input.text

        if Authentication.authenticate(username, password):
            self.callback(True)  # Llama al callback con éxito
            self.dismiss()  # Cierra el popup
        else:
            self.password_input.text = ""  # Limpia el campo de contraseña
            self.username_input.text = ""  # Limpia el campo de usuario

class DemandFactorPopup(Popup):
    """
    Ventana emergente para elegir el factor de demanda.
    """
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.title = "Select Demand Factor"
        self.size_hint = (0.8, 0.4)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.auto_toggle = ToggleButton(text="Auto Demand", group="demand", state="down")
        self.layout.add_widget(self.auto_toggle)

        self.manual_toggle = ToggleButton(text="Manual Demand", group="demand")
        self.layout.add_widget(self.manual_toggle)

        self.manual_input = TextInput(hint_text="Enter demand factor (0.5 to 2.5)", multiline=False)
        self.layout.add_widget(self.manual_input)

        self.confirm_button = Button(text="Confirm", size_hint=(1, 0.3))
        self.confirm_button.bind(on_press=self.confirm_demand)
        self.layout.add_widget(self.confirm_button)

        self.add_widget(self.layout)

    def confirm_demand(self, instance):
        """
        Confirma la selección del factor de demanda.
        """
        if self.auto_toggle.state == "down":
            demand_factor = None  # Auto demand
        else:
            try:
                demand_factor = float(self.manual_input.text)
                if demand_factor < 0.5 or demand_factor > 2.5:
                    raise ValueError("Demand factor out of range.")
            except ValueError:
                self.manual_input.text = "Invalid input"
                return

        self.callback(demand_factor)  # Llama al callback con el factor de demanda
        self.dismiss()  # Cierra el popup

class TaximeterApp(App):
    def build(self):
        """
        Construye la interfaz gráfica de la aplicación.
        """
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Mostrar el popup de autenticación al iniciar
        self.show_login_popup()

        return self.layout

    def show_login_popup(self):
        """
        Muestra el popup de autenticación.
        """
        self.login_popup = LoginPopup(self.on_login_result)
        self.login_popup.open()

    def on_login_result(self, success):
        """
        Callback para manejar el resultado de la autenticación.
        """
        if success:
            logging.info("User logged in successfully.")
            self.show_demand_factor_popup()  # Muestra el popup para elegir el factor de demanda
        else:
            logging.warning("Failed login attempt.")
            self.stop()  # Cierra la aplicación si el login falla

    def show_demand_factor_popup(self):
        """
        Muestra el popup para elegir el factor de demanda.
        """
        self.demand_popup = DemandFactorPopup(self.on_demand_factor_selected)
        self.demand_popup.open()

    def on_demand_factor_selected(self, demand_factor):
        """
        Callback para manejar la selección del factor de demanda.
        """
        self.taximeter = Taximeter(demand_factor=demand_factor)
        self.initialize_app()  # Inicializa la aplicación después de seleccionar el factor de demanda

    def initialize_app(self):
        """
        Inicializa la aplicación después de un login exitoso y selección del factor de demanda.
        """
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
        self.toggle_button = Button(text="Start Trip", font_size=18)
        self.toggle_button.bind(on_press=self.toggle_movement)
        self.layout.add_widget(self.toggle_button)

        # Botón para finalizar el trayecto
        self.finish_button = Button(text="Finish Trip", font_size=18, disabled=True)
        self.finish_button.bind(on_press=self.finish_trip)
        self.layout.add_widget(self.finish_button)

        # Etiqueta para mostrar el costo
        self.cost_label = Label(text="", font_size=18)
        self.layout.add_widget(self.cost_label)

        # Inicializar el contador de tiempo
        self.start_time = None
        self.elapsed_time = timedelta()
        self.clock_event = None

        logging.info("GUI initialized.")

    def toggle_movement(self, instance):
        """
        Cambia el estado del taxi (en movimiento o detenido).
        """
        if self.start_time is None:
            # Iniciar el trayecto
            self.start_time = datetime.now()
            self.clock_event = Clock.schedule_interval(self.update_time, 1)
            self.toggle_button.text = "Stop Trip"
            self.finish_button.disabled = True
        else:
            # Cambiar entre movimiento y detenido
            self.taximeter.toggle_movement()
            new_label = "Taxi Moving" if self.taximeter.taxi_moving else "Taxi Stopped"
            self.status_label.text = new_label
            self.finish_button.disabled = self.taximeter.taxi_moving  # Deshabilitar finalización si el taxi está en movimiento
            logging.info(f"Taxi is now {new_label}.")

    def finish_trip(self, instance):
        """
        Finaliza el trayecto y muestra el costo.
        """
        if self.clock_event:
            self.clock_event.cancel()  # Detener el contador de tiempo
            self.clock_event = None

        cost = self.taximeter.calculate_trip_cost()
        cost_without_vat = cost / (1 + self.taximeter.billing.VAT_RATE)
        self.cost_label.text = f"Cost (without VAT): {cost_without_vat:.2f} €\nCost (with VAT): {cost:.2f} €"
        logging.info(f"Trip cost calculated: {cost:.2f}€")

        # Preguntar si desea realizar otro trayecto
        self.toggle_button.text = "Start New Trip"
        self.toggle_button.disabled = False
        self.finish_button.disabled = True

    def update_time(self, dt):
        """
        Actualiza el contador de tiempo.
        """
        self.elapsed_time = datetime.now() - self.start_time
        self.time_label.text = f"Time: {str(self.elapsed_time).split('.')[0]}"
        self.taximeter.update_time(1)  # Actualiza el tiempo en el taxímetro cada segundo

if __name__ == "__main__":
    logging.info("Application started.")
    TaximeterApp().run()
    logging.info("Application closed.")