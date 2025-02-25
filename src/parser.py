import yaml

def parse_yaml(file_path):
    """
    Parses a YAML file and converts it to a structured dictionary.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return convert_to_list(data)

def parse_yaml_string(yaml_string):
    """
    Parses a YAML string and converts it to a structured dictionary.
    """
    data = yaml.safe_load(yaml_string)
    return convert_to_list(data)

def convert_to_list(structure):
    result = []
    if isinstance(structure, dict):
        for key, value in structure.items():
            if isinstance(value, list):
                result.append({
                    "name": key,
                    "type": "folder",
                    "children": convert_to_list(value)
                })
            else:
                result.append({
                    "name": key,
                    "type": "file"
                })
    elif isinstance(structure, list):
        for item in structure:
            if isinstance(item, dict):
                for key, value in item.items():
                    result.append({
                        "name": key,
                        "type": "folder",
                        "children": convert_to_list(value)
                    })
            else:
                result.append({
                    "name": item,
                    "type": "file"
                })
    return result

def parse_text(file_path):
    """
    Parses a text file to generate a structured dictionary.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    structure = []
    stack = [(structure, -1)]  # Stack to track indentation levels

    for line in lines:
        depth = line.count('│') + line.count('├') + line.count('└')
        name = line.strip().replace('├──', '').replace('└──', '').replace('│', '').strip()

        if not name or name.startswith('#'):
            continue

        item_type = "folder" if name.endswith('/') else "file"
        entry = {"name": name.rstrip('/'), "type": item_type}
        
        while stack and stack[-1][1] >= depth:
            stack.pop()

        parent, _ = stack[-1]
        parent.append(entry)

        if item_type == "folder":
            entry["children"] = []
            stack.append((entry["children"], depth))

    return structure

def parse_structure(file_path):
    """
    Determines the file type (YAML or Text) and parses accordingly.
    """
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return parse_yaml(file_path)
    elif file_path.endswith('.txt'):
        return parse_text(file_path)
    else:
        raise ValueError("Unsupported file format. Use YAML or TXT.")
