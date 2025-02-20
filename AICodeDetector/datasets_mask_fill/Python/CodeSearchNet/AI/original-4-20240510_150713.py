
  if not observations.shape.is_fully_defined():
    raise ValueError('Observations must be fully defined.')

  if not kernel.batch_shape.is_fully_defined():
    raise ValueError('Kernel batch shapes must be fully defined.')

  if not kernel.batch_shape.is_compatible_with(observation_index_points):
    raise ValueError('Observation batch shapes must be compatible with '
                     'observation data.')

  if not kernel.batch_shape.is_compatible_with(observation_index_points):
    raise ValueError('Observation batch shapes must be compatible with '
                     'observation data