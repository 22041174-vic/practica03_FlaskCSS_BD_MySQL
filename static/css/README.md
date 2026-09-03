# Práctica 03 - Flask + Jinja + CSS + MySQL

## Desarrollo Web con Python

Aplicación web desarrollada con **Python, Flask, Jinja, HTML, CSS y MySQL** para registrar y consultar información de clientes.

La práctica permite integrar los conceptos básicos de desarrollo web con el almacenamiento persistente de información en una base de datos MySQL ejecutada inicialmente en `localhost`.

---

## Objetivo

Desarrollar una aplicación web que permita:

- Capturar información de clientes mediante un formulario HTML.
- Enviar los datos del navegador al servidor mediante el método `POST`.
- Recibir y procesar los datos utilizando Flask.
- Utilizar Jinja para generar contenido HTML dinámico.
- Conectarse desde Python a una base de datos MySQL.
- Insertar registros en una tabla de MySQL.
- Consultar los clientes almacenados.
- Mostrar los registros mediante una tabla HTML.
- Separar la lógica de la aplicación de las operaciones de base de datos.

---

## Tecnologías utilizadas

- Python
- Flask
- Jinja
- HTML5
- CSS3
- MySQL
- MySQL Workbench
- mysql-connector-python
- Visual Studio Code

---

## Estructura del proyecto

```text
Practica_03_FLASKCSS_BD_MySQL/
│
├── app.py
├── CMySQL.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── mostrar_cliente.html
│   └── listar_clientes.html
│
└── static/
    └── css/
        └── estilos.css
```

---

## Base de datos

La aplicación utiliza una base de datos MySQL llamada:

```sql
comercio
```

Para seleccionarla:

```sql
USE comercio;
```

La tabla utilizada por la aplicación es:

```sql
clientes
```

### Crear la tabla

```sql
CREATE TABLE clientes (

    id_cliente INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(50) NOT NULL,
    apellido_paterno VARCHAR(50) NOT NULL,
    apellido_materno VARCHAR(50),

    fecha_nacimiento DATE,
    genero VARCHAR(15),

    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),

    estado VARCHAR(50),
    ciudad VARCHAR(50),
    codigo_postal VARCHAR(10),

    tipo_cliente VARCHAR(20),

    intereses VARCHAR(200),

    limite_credito DECIMAL(10,2),

    observaciones VARCHAR(250)

);
```

Para comprobar la estructura:

```sql
DESCRIBE clientes;
```

Para consultar los registros:

```sql
SELECT *
FROM clientes;
```

---

## Entorno virtual

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo debe aparecer:

```text
(.venv)
```

al inicio de la línea de comandos.

---

## Instalación de dependencias

Instalar