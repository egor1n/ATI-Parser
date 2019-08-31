import csv


def read(path_to_read):
    """
    Read a CSV file
    :param path_to_read: -
    :return: -
    """
    with open(path_to_read) as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            print(' '.join(row))


def write(data, path_to_write):
    """
    Write data to a CSV file path
    :param data: -
    :param path_to_write: -
    :return: -
    """
    with open(path_to_write, 'w', newline='') as csv_file:                                                                  # CHECK OPENING MODE
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def write_a(data, path_to_write):
    with open(path_to_write, 'a', newline='') as csv_file:                                                                  # CHECK OPENING MODE
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
