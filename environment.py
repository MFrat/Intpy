import os
import ctypes
import sqlite3

FOLDER_NAME = ".intpy"

def _create_folder():
    os.makedirs(FOLDER_NAME)
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ctypes.windll.kernel32.SetFileAttributesW(FOLDER_NAME, FILE_ATTRIBUTE_HIDDEN)

def init_env(f):
    if _env_exists():
        return f

    _create_folder()
    _create_database()

    return f

def _create_database():
    init_db()

def _create_table():
    conn = sqlite3.connect('.intpy/intpy.db')
    conn.close()

def init_db():
    if not _db_exists():
        _create_table()

def _db_exists():
    return False

def _env_exists():
    return os.path.exists(FOLDER_NAME)