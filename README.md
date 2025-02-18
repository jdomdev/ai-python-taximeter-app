# 🚖 **Taximeter App** - ¡La mejor solución para taxis modernos! 🚖

## 📝 **Descripción del Proyecto**  
¡Bienvenidos a **Taximeter App**, el prototipo de un taxímetro digital revolucionario creado con Python! El objetivo de este proyecto es modernizar el sistema de facturación en los taxis, brindando a los conductores y pasajeros una experiencia de cálculo de tarifas precisa y eficiente. **Taximeter App** no solo simplifica el cálculo de tarifas, sino que también lleva la tecnología a un nuevo nivel con una interfaz gráfica intuitiva y un rendimiento optimizado.

---

## 🛠️ **Tecnologías Utilizadas**  
Hemos llevado la aplicación a un **nivel avanzado**, utilizando las siguientes tecnologías:

- **Python 3.8+** 🐍: El lenguaje potente y versátil para todo tipo de soluciones.
- **Kivy** 🎨: ¡La interfaz gráfica de usuario (GUI) ahora es espectacular! Hemos dejado atrás Tkinter y hemos mejorado la experiencia visual y de interacción con **Kivy**, ofreciendo una interfaz moderna y fluida.
- **Git y GitHub**: Control de versiones de manera eficiente para una colaboración perfecta.
- **Trello**: Gestión del proyecto para mantener todo en orden y alcanzar los hitos más rápido.

---

## 🚀 **Instalación y Uso**  

### **Requisitos Previos**  
Asegúrate de tener instalado lo siguiente:  
- **Python 3.8+** 🐍
- **Git** (opcional, solo si deseas clonar el repositorio)  
- **uv** para la gestión de entornos virtuales

---

### **Instalación con `pip`**  

1. **Clona el repositorio** (si no lo tienes):  
   ```bash
   git clone https://github.com/jdomdev/taximeter-app-python.git
   cd taximeter-app-python
   ```

2. **Crea un entorno virtual** (recomendado):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias con `pip`**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**:  
   ```bash
   python main.py
   ```

---

### **Instalación con `uv`**  

1. **Instala `uv`** (si no lo tienes instalado):  
   ```bash
   pip install uv
   ```

2. **Clona el repositorio** (si no lo tienes):  
   ```bash
   git clone https://github.com/jdomdev/taximeter-app-python.git
   cd taximeter-app-python
   ```

3. **Crea un entorno virtual** (recomendado):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

4. **Instala las dependencias con `uv`**:  
   ```bash
   uv pip install -r requirements.txt
   ```

5. **Ejecuta la aplicación**:  
   ```bash
   python main.py
   ```

---

### **Uso de la Aplicación**  

1. **Iniciar un viaje**:  
   La app te preguntará si deseas iniciar el viaje. Responde `y` para comenzar.

2. **Controlar el taxi**:  
   Durante el trayecto, puedes mover o detener el taxi respondiendo `y` o `n` según sea necesario.

3. **Finalizar el viaje**:  
   Cuando quieras finalizar, responde `y` cuando se te pregunte si deseas terminar. La app calculará el costo total y te mostrará un resumen del viaje.

4. **Nuevo viaje**:  
   Una vez terminado un viaje, puedes iniciar otro sin necesidad de cerrar la aplicación.

---

## 📌 **Estado del Proyecto**  
- 🏗️ **Nivel avanzado**: Se está trabajano en una GUI fluida y optimizada con **Kivy**.
- 🔜 **Próximas mejoras**: Se está trabajando en la integración web y más funcionalidades para la versión estable, que ya está funcionando perfectamente.

---

## 📊 **Niveles de Implementación**

### 🟢 **Nivel Esencial**  
Desarrollar una CLI simple en Python con las funcionalidades básicas:
- Iniciar un viaje y calcular la tarifa (2 céntimos por segundo en parado, 5 céntimos en movimiento).
- Finalizar el viaje y mostrar el total en euros.
- Permitir iniciar un nuevo viaje sin cerrar la aplicación.

### 🟡 **Nivel Medio**  
- **Registro de logs** para trazabilidad.
- **Tests unitarios** para asegurar el correcto funcionamiento.
- **Historial de trayectos** en un archivo de texto.
- Configuración de precios para adaptarse a la demanda.

### 🟠 **Nivel Avanzado**  
- **Refactorización con OOP** para mejorar la arquitectura del código.
- **Interfaz gráfica de usuario (GUI)** moderna y fluida con **Kivy**.
- **Autenticación con contraseñas** para proteger el acceso a la aplicación.

### 🔴 **Nivel Experto**  
- Integración con una base de datos para almacenar trayectos históricos.
- **Dockerización** para facilitar despliegues.
- Desarrollo de una versión web accesible a través de internet.

---

## 📄 **Licencia**  
[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  

Este proyecto está licenciado bajo la **GNU General Public License v3.0**.  
Puedes usarlo, modificarlo y distribuirlo bajo los términos de la licencia.

🔗 **Más información:** [Licencia GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 👨‍💻 **Autor**  
- **Juan Domingo**  
- **Última actualización:** ¡Siempre trabajando en mejoras!

---
