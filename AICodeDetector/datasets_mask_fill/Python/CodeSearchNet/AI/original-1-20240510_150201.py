
    filename = ""
    if hasattr(ti, "log_filename"):
        filename = ti.log_filename

    elif hasattr(ti, "task_id"):
        if hasattr(ti.task_id, "task_id"):
            filename = ti.task_id.task_id.task_id
        else:
            filename = ti.task_id.dag_id.task_id.task_id.task_id.task_id.task_id
    else:
        filename = ti.dag_id.task_id.task_id.task_id.task_id.