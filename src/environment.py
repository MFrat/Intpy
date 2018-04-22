import os
import ctypes
import sqlite3

from src.logger.log import debug

FOLDER_NAME = ".intpy"
CACHE_FOLDER_NAME = FOLDER_NAME + "/cache"
HIDDEN = 0x02


def _create_cache_folder():
    if _cache_folder_exists():
        return

    debug("cache folder doesn't exists, creating one")
    os.makedirs(CACHE_FOLDER_NAME)


def _create_folder():
    debug("creating folder")
    if _folder_exists():
        debug("folder already exists")
        return

    os.makedirs(FOLDER_NAME)
    ctypes.windll.kernel32.SetFileAttributesW(FOLDER_NAME, HIDDEN)
    _create_cache_folder()


def init_env(f):
    debug("cheking if intpy environment exists")
    if _env_exists():
        debug("environment already exists")
        return f

    debug("creating intpy environment")
    _create_folder()
    _create_database()

    return f


def _create_database():
    debug("creating database")
    if _db_exists():
        debug("database already exists")
        return

    _create_table()


def _create_table():
    debug("creating table")
    conn = sqlite3.connect('.intpy/intpy.db')

    stmt = "CREATE TABLE IF NOT EXISTS CACHE (\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
    cache_file TEXT UNIQUE\
    );"

    conn.execute(stmt)

    conn.close()


def _db_exists():
    return os.path.isfile('.intpy/intpy.db')


def _folder_exists():
    return os.path.exists(FOLDER_NAME)


def _cache_folder_exists():
    return os.path.exists(CACHE_FOLDER_NAME)


def _env_exists():
    return _db_exists() and _folder_exists()
