
    DM = models.DagModel
    dag = session.query(DM).filter(DM.dag_id == dag_id).first()
    if dag is None:
        raise DagNotFound("Dag id {} not found".format(dag_id))

    if dag.fileloc and os.path.exists(dag.fileloc):
        raise DagFileExists("Dag id {} is still in DagBag. "
                            "Remove the DAG file first: {}".format(dag_id, dag.fileloc))

    count = 0

    # noinspection PyUnresolvedReferences,PyProtectedMember
    for m in models.base.Base._decl_class_registry.values():
        if hasattr(m, "dag_id"):
       