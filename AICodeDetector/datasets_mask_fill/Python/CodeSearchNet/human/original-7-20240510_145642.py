
    with tf.compat.v1.name_scope(name):
      if isinstance(self._sample_shape, tf.Tensor):
        return self._sample_shape
      return tf.convert_to_tensor(
          value=self.sample_shape.as_list(), dtype=tf.int32)