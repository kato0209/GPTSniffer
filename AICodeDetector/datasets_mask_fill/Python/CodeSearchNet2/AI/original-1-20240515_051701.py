
    if not isinstance(dest_file_path, list):
        dest_file_path = [dest_file_path]

    for path in dest_file_path:
        if not os.path.exists(path):
            raise ValueError("File not found: {}".format(path))

    if not os.path.exists(dest_file_path[0]):
        raise ValueError("File not found: {}".format(dest_file_path[0]))

    if force_download:
        if os.path.exists(dest_file_path[0]):
            raise ValueError("File already exists: {}".