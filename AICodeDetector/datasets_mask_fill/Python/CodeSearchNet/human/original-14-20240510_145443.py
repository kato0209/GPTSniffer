
        conn = self.get_conn()
        self.log.info('Retrieving file from FTP: %s', remote_full_path)
        conn.get(remote_full_path, local_full_path)
        self.log.info('Finished retrieving file from FTP: %s', remote_full_path)