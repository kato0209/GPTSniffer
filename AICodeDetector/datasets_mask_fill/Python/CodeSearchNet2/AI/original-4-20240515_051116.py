
        TI = TaskInstance
        tis = session.query(TI).filter(TI.dag_id == self.dag_id,
                                      TI.execution_date == self.execution_date)
        tis = tis.all()
        for ti in tis:
            if ti.task_id in self.task_ids:
                ti.state = State.SKIPPED
           