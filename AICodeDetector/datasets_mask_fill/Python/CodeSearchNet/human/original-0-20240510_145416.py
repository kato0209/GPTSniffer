
        with tempfile.TemporaryFile() as temp_file:
            if os.path.isdir(path):
                files = [os.path.join(path, name) for name in os.listdir(path)]
            else:
                files = [path]
            with tarfile.open(mode='w:gz', fileobj=temp_file) as tar_file:
                for f in files:
               