def read_file(path: str) -> list:
    """This function reads the contents of a file and returns them as a list.

    Args:
        path (str): The path to the file to be read

    Returns:
        list: A list containing the lines in the file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines: list = file.readlines()
        return lines
    except FileNotFoundError:
        return list()
    