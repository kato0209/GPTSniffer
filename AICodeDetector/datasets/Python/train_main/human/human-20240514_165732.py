

        if self.terminating:
            # ensure termination if processes are created later
            self.task_runner.terminate()
            return

        self.task_instance.refresh_from_db()
        ti = self.task_instance

        fqdn = get_hostname()
        same_hostname = fqdn == ti.hostname
        same_process = ti.pid == os.getpid()

        if ti.state == State.RUNNING:
            if