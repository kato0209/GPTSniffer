
  assertions = _lu_reconstruct_assertions(lower_upper, perm, validate_args)

  message = 'Input `rhs` must have at least 2 dimensions.'
  if rhs.shape.ndims is not None:
    if rhs.shape.ndims < 2:
      raise ValueError(message)
  elif validate_args:
    assertions.append(
        tf.compat.v1.assert_rank_at_least(rhs, rank=2, message=message))

  message = '`lower_upper.shape[-1]` must equal `rhs.shape[-1]`.'
  if (tf.compat.dimension_value(lower_upper.shape[-1]) is not None and
      tf.compat.dimension_value(rhs.shape[-2]) is not None):
    if lower_upper.shape[-1] != rhs.shape[-2]:
      raise ValueError(message)
  elif validate_args:
    assertions.append(
        tf.compat.v1.assert_equal(
            tf.shape(input=lower_upper)[-1],
         