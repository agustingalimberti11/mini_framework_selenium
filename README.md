# 🧪 Mini Framework de Automatización Selenium (Python)

Este proyecto es un ejemplo educativo de un **framework de automatización de pruebas funcional** utilizando:

- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Datos externos (CSV)
- Configuración en YAML
- Reportes HTML
- WebDriver Manager (sin necesidad de instalar ChromeDriver manualmente)

Ideal para estudiantes que inician en automatización profesional.

---

## 📁 Estructura del proyecto

mini_framework/
│
├── tests/ → Scripts de prueba y configuración de Pytest
│ ├── test_login.py
│ └── conftest.py
│
├── pages/ → Page Objects (interacción con la UI)
│ ├── login_page.py
│ └── dashboard_page.py
│
├── data/ → Archivos de datos (CSV)
│ └── users.csv
│
├── config/ → Configuración general del proyecto
│ └── config.yaml
│
├── utils/ → Funciones reutilizables
│ └── browser_factory.py
│
├── reports/ → Aquí se guardan los reportes HTML de ejecución
│
├── run_tests.sh → Script de ejecución automatizada (Linux/macOS)
├── requirements.txt → Dependencias del proyecto
└── README.md → Este archivo

yaml
Copiar
Editar

---

## 🔧 Requisitos previos

### Instalación de dependencias

1. Cloná o descomprimí el proyecto en tu computadora.
2. Abrí una terminal (o la consola de PyCharm) en la carpeta del proyecto.
3. Ejecutá:

```bash
pip install -r requirements.txt
Esto instalará:

selenium

pytest

pyyaml

webdriver-manager

pytest-html

✅ Cómo ejecutar el test de login
Este framework está preconfigurado para usar el sitio público de pruebas:
🔗 https://opensource-demo.orangehrmlive.com/

Ejecutar pruebas:
bash
Copiar
Editar
pytest --html=reports/report.html --self-contained-html
Esto:

Abre el navegador Chrome.

Accede al sitio de prueba.

Realiza un login con usuario: Admin y clave: admin123.

Verifica si llegó al Dashboard.

Genera un reporte en reports/report.html.

🧠 ¿Qué podés modificar?
Usuario y contraseña: están en data/users.csv.

URL del sistema: se configura desde config/config.yaml.

Headless o no: también se ajusta desde config.yaml.

Navegador: por ahora usa Chrome, pero podés adaptar fácilmente browser_factory.py para Firefox.

🚀 Siguientes pasos sugeridos
Crear más pruebas (login incorrecto, logout, navegación).

Implementar lectura automática desde CSV para múltiples combinaciones.

Agregar nuevos Page Objects (dashboard, menú, etc).

Configurar integración continua con GitHub Actions o Jenkins.

🛠 ¿Problemas comunes?
El navegador no abre: Asegurate de tener Chrome instalado. El driver se descarga automáticamente con webdriver-manager.

URL no encontrada: Revisá config.yaml y que tengas internet.

ImportError (utils, pages): Asegurate de tener los archivos __init__.py en cada carpeta.

Windows: ejecutá siempre pytest desde PowerShell o terminal integrada (no uses bash run_tests.sh).