# 🚖 **Taximeter App** – El Futuro del Taxímetro Digital  

¡Bienvenido a **Taximeter App**! 🎉 Un innovador sistema digital para calcular tarifas de taxi con precisión y eficiencia. Olvídate de las tenologías anteriores y moderniza tu servicio con este software basado en **Python**.  

📢 **Actualmente en Nivel Medio**: Logs y tests unitarios implementados.  
🚀 **Próxima meta**: **Nivel Experto** con base de datos, Docker y versión web. ¡Estamos trabajando en ello!  

---  

## 🛠️ **Tecnologías Utilizadas**  
✅ **Python** 🐍  
✅ **Interfaz CLI interactiva**  
✅ **Logs para trazabilidad** 📜  
✅ **Tests unitarios** 🧪  
✅ **Git y GitHub** para control de versiones 🖥️  
✅ **Gestión con `pyproject.toml` y `uv`** 📦  

🚀 **Próximos avances** (Nivel Experto):  
🔹 Integración con base de datos (SQLite/PostgreSQL)  
🔹 Dockerización para despliegue eficiente 🐳  
🔹 Versión web con Flask/Django 🌍  

---

## 📥 **Descarga e Instalación**  

💻 Compatible con **Windows, Linux y macOS**.  

### **🔹 Opción 1: Instalación con `uv` (Recomendada)**
`uv` es más rápido que `pip` y maneja dependencias de forma optimizada.  

#### **Instalación en Linux/macOS** 🐧🍏  
```bash
# Instala `uv` si no lo tienes
pip install uv

# Clona el repositorio y accede a la carpeta
git clone https://github.com/jdomdev/taximeter-app-python.git
cd taximeter-app-python

# Crea un entorno virtual y actívalo
uv venv venv
source venv/bin/activate

# Instala las dependencias
uv add <dependency>
```

#### **Instalación en Windows** 🖥️  
```powershell
# Instala `uv` si no lo tienes
pip install uv

# Clona el repositorio y accede a la carpeta
git clone https://github.com/jdomdev/taximeter-app-python.git
cd taximeter-app-python

# Crea un entorno virtual y actívalo
uv venv venv
venv\Scripts\activate

# Instala las dependencias
uv <dependency>
```

🔹 **Ejecutar la aplicación**  
```bash
python main.py
```

---

### **🔹 Opción 2: Instalación con `pip` (Alternativa)**  
Si prefieres usar `pip`, sigue estos pasos:  

#### **Instalación en Linux/macOS** 🐧🍏  
```bash
# Clona el repositorio y accede a la carpeta
git clone https://github.com/jdomdev/taximeter-app-python.git
cd taximeter-app-python

# Crea un entorno virtual y actívalo
python -m venv venv
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt
```

#### **Instalación en Windows** 🖥️  
```powershell
# Clona el repositorio y accede a la carpeta
git clone https://github.com/jdomdev/taximeter-app-python.git
cd taximeter-app-python

# Crea un entorno virtual y actívalo
python -m venv venv
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt
```

🔹 **Ejecutar la aplicación**  
```bash
python main.py
```

---

## 🎯 **Cómo Usar Taximeter App**  
1️⃣ **Inicia el taxímetro** con un clic 🏁 
2️⃣ **Mueve o detén el taxi** para medir el tiempo y la tarifa 🕒  
3️⃣ **Calcula el costo del viaje** automáticamente 💰  
4️⃣ **Consulta el historial de trayectos** en los registros 📜  

---

## 📊 **Estado del Proyecto**  

### **✅ Nivel Medio - Completado**  
✔️ Programa interactivo en CLI  
✔️ Logs de actividad y autenticación  
✔️ Tests unitarios con `unittest`  
✔️ Registro de trayectos en archivos  

### **🚀 Próximo Objetivo - Nivel Experto**  
🔹 Integración con bases de datos 🗄️  
🔹 API REST con Flask/Django 🌐  
🔹 Dockerización para despliegue ⚙️  


---

## 📊 Niveles de Implementación  

### 🟢 Nivel Esencial  
- Desarrollar un programa CLI (Interfaz de Línea de Comandos) en Python.  
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

## 📄 **Licencia**  
[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  

Este proyecto está licenciado bajo la **GNU General Public License v3.0**. Puedes usarlo, modificarlo y distribuirlo bajo los términos de la licencia.  

🔗 **Más información:** [Licencia GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)  

---

## 👨‍💻 **Autor**  
👤 **Juan Domingo**  
📅 **Actualizado constantemente hasta la entrega final.**  

¡🚖 Únete a la revolución del taxímetro digital y prueba **Taximeter App** hoy mismo! 🚀  
