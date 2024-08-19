import os
import sqlite3


def ObtenerConexion():
    # Ensure the directory exists
    db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/historialDatos'))
    os.makedirs(db_dir, exist_ok=True)

    # Use an absolute path for the database file
    db_path = os.path.join(db_dir, 'telegram_bot.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor

def obtenerCodigoVerificacion():
    conn, cursor = ObtenerConexion()
    cursor.execute('SELECT codigo_verificacion FROM users LIMIT 1')
    row = cursor.fetchone()
    if row:
        return row[0]  # Return the verification code as a string
    return None

def obtenerTelefono():
    conn, cursor = ObtenerConexion()
    cursor.execute('SELECT phone_number FROM users LIMIT 1')
    row = cursor.fetchone()
    if row:
        return row[0]  # Return the phone number as a string
    return None
def obtenerToken():
    # Ensure this function returns a string, not a tuple
    conn, cursor = ObtenerConexion()
    cursor.execute('SELECT token FROM users LIMIT 1')
    row = cursor.fetchone()
    if row:
        return row[0]  # Return the token as a string
    return None
def darComoVerificado():
    conn, cursor = ObtenerConexion()
    cursor.execute('UPDATE users SET verified = 1')
    conn.commit()
    conn.close()
    return None
def eliminarCodigoVerificacion():
    conn, cursor = ObtenerConexion()
    cursor.execute('UPDATE users SET codigo_verificacion = ""')
    conn.commit()
    conn.close()


def comprobarVerificado():
    conn, cursor = ObtenerConexion()
    cursor.execute('SELECT verified FROM users LIMIT 1')
    row = cursor.fetchone()
    if row:
        return row[0] == 1





def check_and_add_chat_id_column():
    conn, cursor = ObtenerConexion()
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'chat_id' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN chat_id INTEGER")
        conn.commit()

    conn.close()


def añadirChatId(chat_id):
    check_and_add_chat_id_column()
    conn, cursor = ObtenerConexion()
    cursor.execute('UPDATE users SET chat_id = ?', (chat_id,))
    conn.commit()
    conn.close()

def obtenerChatId():
    conn, cursor = ObtenerConexion()
    cursor.execute('SELECT chat_id FROM users LIMIT 1')
    row = cursor.fetchone()
    if row:
        return row[0]
    return None

def verificar_chat_id(chat_id):
    conn, cursor = ObtenerConexion()
    cursor.execute('SELECT chat_id FROM users WHERE chat_id = ?', (chat_id,))
    row = cursor.fetchone()
    if row:
        return True
    return False