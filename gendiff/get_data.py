
def get_data_from_file(file_path):

    data = open(file_path)
    extension = file_path.split('.')[1]
    return data, extension
