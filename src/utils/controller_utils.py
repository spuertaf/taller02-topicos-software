from socket import gethostname

from docker import from_env


def cut_json(json: dict, *args) -> dict:
    return dict((key, json[key]) for key in args)


def get_host_info() -> dict:
    try:
        client = from_env()
        container_id = client.containers.get(gethostname())
        host: str = container_id
    except Exception as e:
        print(f"Error fetching the container's ID {e}")
        host: str = gethostname()
    finally:
        return {
            "host": host
        }
        
    
def merge_dicts(*args) -> dict:
    merged_dicts: dict = {}
    for arg in args:
        assert isinstance(arg, dict), f"arg must be dict not {type(arg)}"
        merged_dicts.update(arg)
    return merged_dicts