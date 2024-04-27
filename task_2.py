from read_file import read_file

def get_cats_info(path):
    list_of_cats = list()
    lines = read_file(path)
    for line in lines:
        cat_id, name, age = line.split(",")
        list_of_cats.append({"id": cat_id, "name": name, "age": age.removesuffix('\n')})

    return list_of_cats


if __name__ == "__main__":
    print(get_cats_info('task_2/cats.txt'))