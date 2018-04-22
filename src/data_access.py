import pickle
import sqlite3

from .environment import init_env
from .logger.log import debug


def _create_conn():
    return sqlite3.connect('.intpy/intpy.db')


def _close_conn(conn):
    conn.close()


def _exec_stmt(stmt):
    conn = _create_conn()
    conn.execute(stmt)
    conn.commit()
    conn.close()


def _exec_stmt_return(stmt):
    conn = _create_conn()
    cursor = conn.execute(stmt)
    return cursor.fetchone()


def _save(file_name):
    _exec_stmt("INSERT INTO CACHE(cache_file) VALUES ('{0}')".format(file_name.replace("'", "").replace('"', "")))


def _get(id):
    return _exec_stmt_return("SELECT cache_file FROM CACHE WHERE cache_file = '{0}'".format(id.replace("'", "").
                                                                                            replace('"', "")))


def _format_args(args):
    return str([str(x).replace('"', "").replace("'", "") for x in args])


def _get_file_name(id):
    return "{0}.{1}".format(id, "ipcache")


def _get_id(fun_name, fun_args):
    return fun_name + _format_args(fun_args)


@init_env
def get_cache_data(fun_name, fun_args):
    id = _get_id(fun_name, fun_args)
    file_name = _get(_get_file_name(id))

    def deserialize(id):
        with open(".intpy/cache/{0}".format(_get_file_name(id)), 'rb') as file:
            return pickle.load(file)

    return deserialize(id) if file_name is not None else None


def create_entry(fun_name, fun_args, fun_return, elapsed_time):
    id = _get_id(fun_name, fun_args)

    def serialize(return_value, file_name):
        with open(".intpy/cache/{0}".format(_get_file_name(file_name)), 'wb') as file:
            return pickle.dump(return_value, file, protocol=pickle.HIGHEST_PROTOCOL)

    debug("serializing return value from {0}".format(fun_name))
    serialize(fun_return, id)

    debug("inserting reference in database")
    _save(_get_file_name(id))
