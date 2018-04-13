class Interceptor(object):

    def __getattribute__(self,name):
        attr = object.__getattribute__(self, name)
        if hasattr(attr, '__call__') and attr.__name__ == "func":
            def cached_return(*args, **kwargs):
                return "cache hit! {0}".format(attr.__name__)

            return cached_return
        else:
            return attr