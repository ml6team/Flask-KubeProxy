class KubeProxy(object):
    """Fixes swagger.json behavior behind kubernetes proxy.
    The HTTP_X_FORWARDED_URI header added by the proxy is converted and
    saved as SCRIPT_NAME in environ.
    SCRIPT_NAME is used to build the path for the swagger.json file and the
    urls for the 'try it out' swagger functionality.

    Args:
        app: the WSGI application
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        proxy_path = environ.get('HTTP_X_FORWARDED_URI', '')
        path_info = environ.get('PATH_INFO', '')
        if proxy_path.endswith(path_info):
            proxy_path = proxy_path[:-len(path_info)]
        environ['SCRIPT_NAME'] = proxy_path

        return self.app(environ, start_response)