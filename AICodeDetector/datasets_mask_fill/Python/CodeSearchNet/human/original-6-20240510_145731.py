
  with tf.name_scope(name or 'maybe_validate_perm'):
    assertions = []
    if not dtype_util.is_integer(perm.dtype):
      raise TypeError('`perm` must be integer type')

    msg = '`perm` must be a vector.'
    if tensorshape_util.rank(perm.shape) is not None:
      if tensorshape_util.rank(perm.shape) != 1:
        raise ValueError(
            msg[:-1] +
            ', saw rank: {}.'.format(tensorshape_util.rank(perm.shape)))
    elif validate_args:
      assertions += [assert_util.assert_rank(perm, 1, message=msg)]

    perm_ = tf.get_static_value(perm)
    msg = '`perm` must be a valid permutation vector.'
  