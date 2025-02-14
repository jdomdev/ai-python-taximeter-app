# 🚖 Taximeter App  

## 📝 Descripción del Proyecto  
Este proyecto consiste en desarrollar un prototipo de taxímetro digital utilizando Python. El objetivo es modernizar el sistema de facturación de los taxis y crear un sistema que calcule las tarifas a cobrar a los clientes de manera precisa y eficiente.  

---

## 🛠️ Tecnologías Utilizadas  
- **Python** 🐍  
- **Git y GitHub** para control de versiones  
- **Trello o Jira** para gestión del proyecto  
- **Bibliotecas adicionales** según el nivel de implementación:  
  - `logging`, `unittest` (Nivel Medio)  
  - `tkinter`, `SQLite` (Nivel Avanzado)  
  - `Docker`, `Flask/Django` (Nivel Experto)  

---

## 🚀 Instalación y Uso  

### **Requisitos Previos**  
Asegúrate de tener instalado:  
- **Python 3.8+** 🐍  
- **Git** (opcional, para clonar el repositorio)  

---

### **Instalación con `pip`**  

1. **Clona el repositorio** (opcional si ya tienes el código):  
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
   python taximeter.py
   ```

---

### **Instalación con `uv`**  

1. **Instala `uv`** (si no lo tienes instalado):  
   ```bash
   pip install uv
   ```

2. **Clona el repositorio** (opcional si ya tienes el código):  
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
   python taximeter.py
   ```

---

### **Uso de la Aplicación**  

1. **Iniciar un viaje**:  
   - La aplicación te preguntará si deseas iniciar el viaje. Responde `y` para comenzar.  

2. **Controlar el taxi**:  
   - Durante el viaje, la aplicación te preguntará si deseas mover o detener el taxi. Responde `y` o `n` según sea necesario.  

3. **Finalizar el viaje**:  
   - Cuando desees finalizar el viaje, responde `y` cuando se te pregunte si deseas terminar el trayecto.  
   - La aplicación calculará el costo total y mostrará un resumen del viaje.  

4. **Iniciar un nuevo viaje**:  
   - Después de finalizar un viaje, puedes iniciar uno nuevo sin cerrar la aplicación.  

---

## 📌 Estado del Proyecto  
🏗️ Nivel avanzado en proceso.  
🔜 Próximas mejoras en los niveles siguientes.  

---

## 📊 Niveles de Implementación  

### 🟢 Nivel Esencial  
Desarrollar un programa CLI (Interfaz de Línea de Comandos) en Python.
- Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
- Implementar las siguientes funcionalidades básicas:
  - Iniciar un trayecto.
  - Calcular tarifa mientras el taxi está parado (2 céntimos por segundo).
  - Calcular tarifa mientras el taxi está en movimiento (5 céntimos por segundo).
  - Finalizar un trayecto y mostrar el total en euros.
  - Permitir iniciar un nuevo trayecto sin cerrar el programa.

### 🟡 Nivel Medio  
- Implementar un sistema de logs para la trazabilidad del código.
- Agregar tests unitarios para asegurar el correcto funcionamiento del programa.
- Crear un registro histórico de trayectos pasados en un archivo de texto plano.
- Permitir la configuración de precios para adaptarse a la demanda actual.

### 🟠 Nivel Avanzado  
- Refactorizar el código utilizando un enfoque orientado a objetos (OOP).
- Implementar un sistema de autenticación con contraseñas para proteger el acceso al programa.
- Desarrollar una interfaz gráfica de usuario (GUI) para hacer el programa más amigable. 

### 🔴 Nivel Experto  
- Integrar una base de datos para almacenar los registros de trayectos pasados.
- Dockerizar la aplicación para facilitar su despliegue y portabilidad.
- Desarrollar una versión web de la aplicación accesible a través de internet.

---

## 📄 Licencia  

[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  

Este proyecto está licenciado bajo la **GNU General Public License v3.0**.  
Puedes usarlo, modificarlo y distribuirlo bajo los términos de la licencia.  

🔗 **Más información:** [Licencia GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)  

---

## 👨‍💻 Autor  
- **Juan Domingo**  
- **Última actualización:** A diario hasta la fecha de entrega del proyecto.  

---
