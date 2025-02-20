
  if not callable(true_fn):
    raise TypeError('`true_fn` must be callable.')
  if not callable(false_fn):
    raise TypeError('`false_fn` must be callable.')

  pred_value = _get_static_predicate(pred)
  if pred_value is not None:
    if pred_value:
      return true_fn()
    else:
      return false_fn()
  else:
    return tf.cond(pred=pred, true_fn=true_fn, false_fn=false_fn, name=name)