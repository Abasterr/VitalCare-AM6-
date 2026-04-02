# 🏥 VitalCare - Sistema de Gestión Clínica

**VitalCare** es una plataforma web integral desarrollada con **Django 6.0**, diseñada para la administración eficiente de centros médicos. El sistema permite la gestión completa de pacientes, personal médico, especialidades y el agendamiento de horas, integrando una base de datos robusta y una interfaz moderna y amigable.

---

## 🚀 Características del Proyecto (Cumplimiento de Actividad)

### 1. Entorno de Desarrollo y Seguridad
*   **Virtualenv:** Proyecto aislado en un entorno virtual propio (`venv`).
*   **Cifrado BCrypt:** Implementación de `BCryptSHA256PasswordHasher` para el almacenamiento seguro de contraseñas de usuarios.
*   **Seguridad de Credenciales:** Uso de `python-decouple` para gestionar claves secretas y datos de conexión a la DB mediante un archivo `.env`.

### 2. Base de Datos Relacional (PostgreSQL)
*   **Motor de Base de Datos:** Configuración completa con **PostgreSQL** mediante el driver `psycopg2`.
*   **Modelo de Datos:** Implementación de relaciones `ForeignKey` con integridad referencial (`on_delete=models.CASCADE`) y nombres relacionados para consultas inversas eficientes.

### 3. Lógica de Negocio y Estándar DRY
*   **Clase Abstracta `Persona`:** Centralización de campos comunes (`nombre`, `apellido`, `fecha_nacimiento`) y el método de **cálculo de edad** para evitar duplicidad de código en `Doctor` y `Paciente`.
*   **Gestión de Citas:** Sistema de agenda con selección de estados (Pendiente, Realizada, Cancelada) mediante `choices` de Django.

### 4. Interfaz de Usuario (Bootstrap & UX)
*   **Bootstrap 5:** Uso extensivo de componentes como Cards, Tables, Navbars y Modals para una experiencia responsiva.
*   **Estilo Personalizado (Pantone):** Implementación de una paleta de colores corporativa (`--pantone-primary`, `--pantone-secondary`, etc.) definida en variables CSS.
*   **Iconografía Amigable:** Integración de **FontAwesome 6** para facilitar la identificación visual de acciones (Editar, Borrar, Registrar).

### 5. Administración y Roles de Usuario
*   **Panel de Administración:** Personalización de `admin.py` con clases que heredan de `PersonaAdmin` para mostrar la edad calculada y filtros por especialidad.
*   **Gestión de Usuarios Privada:** El registro de nuevos usuarios está restringido a **Superusuarios** mediante `UserPassesTestMixin`. 
*   **Formulario de Registro Avanzado:** Permite al administrador decidir si el nuevo usuario tendrá permisos de staff/superuser mediante un interruptor visual.

### 6. Panel de Control (Dashboard)
*   **Métricas en Tiempo Real:** Visualización dinámica del total de pacientes, doctores y citas agendadas.
*   **Tarjetas Accionables:** Navegación fluida desde los contadores hacia los listados maestros.
*   **Resumen de Citas:** Tabla de próximas consultas pendientes con contador visual morado para una gestión rápida.

---

## 🛠️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd VitalCare
    ```

2.  **Activar Entorno Virtual:**
    ```bash
    .\venv\Scripts\activate
    ```

3.  **Configurar el archivo .env:**
    Crear un archivo `.env` en la raíz con los siguientes parámetros:
    ```env
    SECRET_KEY=django-insecure-tu-clave
    DB_NAME=nombre_db
    DB_USER=usuario_postgres
    DB_PASSWORD=tu_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

4.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Migrar Base de Datos e Iniciar:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## ✒️ Autor
*   **Alfonso** - *Desarrollo Full Stack* - [Kibernum]

---
*Este proyecto fue desarrollado como parte de la Actividad del Módulo 6 de Django Avanzado.*
