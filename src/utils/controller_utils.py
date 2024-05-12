import os


def cut_json(json: dict, *args) -> dict:
    return dict((key, json[key]) for key in args)


def get_host_info() -> dict:
    host = os.uname()[1]
    return {
        "host":host
    }
        
    
def merge_dicts(*args) -> dict:
    merged_dicts: dict = {}
    for arg in args:
        assert isinstance(arg, dict), f"arg must be dict not {type(arg)}"
        merged_dicts.update(arg)
    return merged_dicts