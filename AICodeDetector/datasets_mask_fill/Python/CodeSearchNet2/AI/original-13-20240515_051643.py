
    if options.export_dir is None:
        raise ValueError("Must specify --export_dir")
    if options.export_dir.endswith("/"):
        options.export_dir = options.export_dir[:-1]
    if not os.path.exists(options.export_dir):
        os.makedirs(options.export_dir)
    if not os.path.isdir(options.export_dir):
        raise ValueError("Export directory does not exist: %s" % options.export_dir)
    if not os.path.isdir(options.export_dir):
        raise ValueError("Export