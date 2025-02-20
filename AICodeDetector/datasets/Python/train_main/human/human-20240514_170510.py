
  with tf.compat.v1.name_scope(name, 'value_and_gradients',
                               [fn_arg_list, result, grads]):

    def _convert_to_tensor(x, name):
      ctt = lambda x_: x_ if x_ is None else tf.convert_to_tensor(
          value=x_, name=name)
      return [ctt(x_) for x_ in x] if is_list_like(x) else ctt(x)

    fn_arg_list = (list(fn_arg_list) if is_list_like(fn_arg_list)
                   else [fn_arg_list])
    fn_arg_list = _convert_to_tensor(fn_arg_list, 'fn_arg')

    if result is None:
