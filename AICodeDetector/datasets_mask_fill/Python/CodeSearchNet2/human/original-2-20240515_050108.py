
  with tf.compat.v1.name_scope(name, 'event_size', [event_shape]):
    event_shape = tf.convert_to_tensor(
        value=event_shape, dtype=tf.int32, name='event_shape')

    event_shape_const = tf.get_static_value(event_shape)
    if event_shape_const is not None:
      return np.prod(event_shape_const)
    else:
      return tf.reduce_prod(input_tensor=event_shape)