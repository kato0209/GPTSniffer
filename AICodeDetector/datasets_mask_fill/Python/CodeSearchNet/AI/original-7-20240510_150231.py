
        try:
            self.log.debug('Checking if file exists: %s', file_path)
            return self.connection.exists(file_path)
        except AzureMissingResourceHttpError:
            self.log.debug('File %s does not exist, will create it.', file_path)
            try:
                self.connection.create_file(file_path)
                return True
            except AzureConflictHttpError:
  