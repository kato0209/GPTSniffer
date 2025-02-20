
    if info_only:
        raise NotImplementedError('info_only=True is not supported anymore')
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if merge:
        cmd = ['ffmpeg', '-i', video_id, '-c', 'copy', '-bsf:v', '0', '-map', '0:v', '1:a', '-map', '0:a', 'copy', output_dir]