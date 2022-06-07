"""
Validates configuration YAML file
"""
def validate_yaml(config):
    if("z_min" not in config or "z_max" not in config):
        raise Exception("YAML is invalid format!")
    if(config["z_min"] is None or config["z_max"] is None):
        raise Exception("YAML is invalid format!") 