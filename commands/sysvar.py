# Lists out all variables stored by Gminal

def execute(core):
    try:
        variables, instance_attr = core.get_vars()
    except ValueError:
        error = core.get_vars()
        print(error)
        return 0
    for var_name, var_content in {**variables, **instance_attr}.items():
        if var_name.startswith('__') and var_name.endswith('__'):
            continue  # Skipping built-in variables
        print(f"{var_name} = {var_content}")
