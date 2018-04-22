import pickle

from .environment import init_env
from .logger.log import debug


def _create_conn():
    # TODO
    pass


def _close_conn(conn):
    # TODO
    pass


def _save(id, entry):
    # TODO
    pass


def _get(id):
    # TODO
    pass


def _format_args(args):
    s = ''
    for i in args:
        s += str(i) + ";"
    
    return s


def _get_id(fun_name, fun_args):
    return fun_name + _format_args(fun_args)


@init_env
def get_cache_data(fun_name, fun_args):
    id = _get_id(fun_name, fun_args)
    # FIXME ir no banco
    return "cache" if fun_name == "func" else None


def create_entry(fun_name, fun_args, fun_return, elapsed_time):
    id = _get_id(fun_name, fun_args)

    def serialize(return_value, file_name):
        with open(".intpy/cache/{0}.{1}".format(file_name, 'ipcache'), 'wb') as file:
            return pickle.dump(return_value, file, protocol=pickle.HIGHEST_PROTOCOL)

    debug("serializing return value from {0}".format(fun_name))
    serialize(fun_return, id)

    debug("recording in database")



