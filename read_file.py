def read_file(path: str) -> list:
    """_summary_

    Args:
        path (str): _description_

    Returns:
        list: _description_
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines: list = file.readlines()
        return lines
    except FileNotFoundError:
        return list()
    