
    if data_type == "train":
        data_path = os.path.join(location, "mnist.pkl.gz")
        if not os.path.exists(data_path):
            download(sc, data_path)
        with gzip.open(data_path, 'rb') as f:
            train_set, valid_set, test_set = cPickle.load(f)
    elif data_type == "test":
        data_path = os.path.join(location, "mnist.pkl.gz")
        if not os.path.exists(data_path):