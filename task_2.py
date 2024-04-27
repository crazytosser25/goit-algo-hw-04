from read_file import read_file

def get_cats_info(path: str) -> list:
    """This function reads a file containing information about cats,
    parses each line, and returns a list of dictionaries with cat id, name, and age.

    Args:
        path (str): The path to the file containing cat information

    Returns:
        list: A list of dictionaries with cat information
    """
    list_of_cats = list()
    lines = read_file(path)
    for line in lines:
        cat_id, name, age = line.split(",")
        list_of_cats.append({"id": cat_id, "name": name, "age": age.removesuffix('\n')})

    return list_of_cats


if __name__ == "__main__":
    print(get_cats_info('task_2/cats.txt'))
