from functools import wraps

PORTS_IN_USE = [1500, 1834, 7777]


def validate_port(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call `func` and store the result
        result = func(*args, **kwargs)
        ip_addr, port = result

        if port < 1024:
            raise ValueError("Cannot use privileged ports below 1024")
        elif port in PORTS_IN_USE:
            raise RuntimeError(f"Port {port} is already in use")

        # if there were no errors, return the result
        return result
    return wrapper


@validate_port
def get_server_addr(ip_addr, port):
    """Return IP address and port of server."""
    return (ip_addr, port)


@validate_port
def get_proxy_addr(ip_addr, port):
    """Return IP address and port of proxy."""
    return (ip_addr, port)


if __name__ == '__main__':
    print(get_server_addr('192.168.1.0', 8080))
    print(get_proxy_addr('127.0.0.1', 12253))
