
    if dag_id not in dagbag.dags:
        return

    execution_date = datetime.now()
    run_id = "manual__{0}".format(execution_date.isoformat())

    dr = DagRun.find(dag_id=dag_id, run_id=run_id)
    if dr:
        logging.info("Dag run already exists for dag_id %s", dag_id)
        raise AirflowException("Dag run for dag_id {} already exists".format(dag_id))

    execution_date = timezone.utcnow()
    dr = DagRun.find(