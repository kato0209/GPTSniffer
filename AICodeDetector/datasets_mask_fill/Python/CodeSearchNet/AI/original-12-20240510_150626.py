
  x = ops.convert_to_tensor(x, name="x")
  if x.dtype.is_integer:
    return math_ops.reduce_sum(math_ops.log(x), axis)
  if axis is not None:
    axis = ops.convert_to_tensor(axis, name="axis")
    return math_ops.reduce_sum(
        math_ops.multiply(x, math_ops.log(axis)), axis, keepdims=True)


def _sum_squares_sum(x, axis=None, keep_dims=False, name=