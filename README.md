
# 🚖 Taximeter App  

## 📝 Descripción del Proyecto  
Este proyecto consiste en desarrollar un prototipo de taxímetro digital utilizando Python. El objetivo es modernizar el sistema de facturación de los taxis y crear un sistema que calcule las tarifas a cobrar a los clientes de manera precisa y eficiente.  

## 📊 Niveles de Implementación  

### 🟢 Nivel Esencial  
La primera versión funcional del taxímetro digital con las siguientes características:  
- Programa CLI (Interfaz de Línea de Comandos) en Python.  
- Bienvenida y explicación del funcionamiento.  
- Cálculo de tarifas basado en:  
  - **Taxi parado:** 2 céntimos por segundo.  
  - **Taxi en movimiento:** 5 céntimos por segundo.  
- Finalización del trayecto con cálculo del total.  
- Opción para iniciar nuevos trayectos sin cerrar el programa.  

### 🟡 Nivel Medio
En futuras versiones se planea:  
- Implementar un sistema de logs para trazabilidad del código.  
- Agregar tests unitarios para verificar el correcto funcionamiento.  
- Guardar un historial de trayectos en un archivo de texto.  
- Permitir la configuración de tarifas de acuerdo con la demanda.  

### 🟠 Nivel Avanzado
Para una versión más robusta, se considera:  
- Refactorización del código utilizando Programación Orientada a Objetos (OOP).  
- Implementación de autenticación con contraseñas para el acceso.  
- Creación de una interfaz gráfica (GUI) para una mejor experiencia de usuario.  

### 🔴 Nivel Experto
En una etapa avanzada, se prevé:  
- Integración con una base de datos para almacenar registros de trayectos.  
- Dockerización de la aplicación para facilitar su despliegue y portabilidad.  
- Desarrollo de una versión web utilizando un framework como Flask o Django.  

## 🛠️ Tecnologías Utilizadas  
- **Python** 🐍  
- **Git y GitHub** para control de versiones  
- **Trello o Jira** para gestión del proyecto  
- **Bibliotecas adicionales** según el nivel de implementación:  
  - `logging`, `unittest` (Nivel Medio)  
  - `tkinter`, `SQLite` (Nivel Avanzado)  
  - `Docker`, `Flask/Django` (Nivel Experto)  

## 🚀 Instalación y Uso  
1. Clona el repositorio:  
   ```bash
   git clone https://github.com/jdomdev/taximeter-app-python.git
   cd taximeter-app-python
   ```
2. Instala las dependencias necesarias:  
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el programa:  
   ```bash
   python taximeter.py
   ```  

## 📌 Estado del Proyecto  
🏗️ Nivel esencial en proceso.  
🔜 Próximas mejoras en los niveles siguientes.  

---

📌 **Autor:** Juan Domingo  
📅 **Última actualización:** a diario hasta fecha de entrega del proyecto.  


Aquí tienes el código Bash para instalar la configuración del proyecto desde `environment.yml`.

---

### **📜 Código Bash para instalar dependencias desde `environment.yml`**  
Guárdalo en un archivo `install.sh` o ejecútalo directamente en la terminal:  
```bash
#!/bin/bash

# Nombre del entorno
ENV_NAME="taximeter-env"

echo "🚀 Creando el entorno de Anaconda desde environment.yml..."
conda env create -f environment.yml

echo "🔄 Activando el entorno $ENV_NAME..."
conda activate $ENV_NAME

echo "✅ Instalación completada. Ya puedes ejecutar el proyecto."
```
**Ejecutar el script:**  
```bash
bash install.sh
```
---


# 🛡️ Licencia - GNU General Public License v3.0  

[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  

Este proyecto está licenciado bajo la **GNU General Public License v3.0**.  
Puedes usarlo, modificarlo y distribuirlo bajo los términos de la licencia.  

🔗 **Más información:** [Licencia GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)  

