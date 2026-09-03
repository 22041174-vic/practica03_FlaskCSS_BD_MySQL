import mysql.connector
import os

# =========================================================
# CONEXIÓN A MYSQL
# =========================================================
def f_conectar():
    conexion = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        port=int(os.environ.get("MYSQL_PORT", 3306)),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE")
    )
    return conexion


# =========================================================
# AGREGAR CLIENTE
# =========================================================
def f_agregar_registro(
    nombre,
    apellido_paterno,
    apellido_materno,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    estado,
    ciudad,
    codigo_postal,
    tipo_cliente,
    intereses,
    limite_credito,
    observaciones
):

    conexion = f_conectar()

    cursor = conexion.cursor()

    sql = """
        INSERT INTO clientes
        (
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s
        )
    """

    valores = (
        nombre,
        apellido_paterno,
        apellido_materno,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        estado,
        ciudad,
        codigo_postal,
        tipo_cliente,
        intereses,
        limite_credito,
        observaciones
    )

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================================================
# LISTAR CLIENTES
# =========================================================
def f_listar_clientes():

    conexion = f_conectar()

    cursor = conexion.cursor()

    sql = """
        SELECT
            id_cliente,
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        FROM clientes
        ORDER BY id_cliente
    """

    cursor.execute(sql)

    clientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return clientes
