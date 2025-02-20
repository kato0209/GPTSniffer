
  state = leapfrog_step_state.state
  state_grads = leapfrog_step_state.state_grads
  momentum = leapfrog_step_state.momentum
  step_size = maybe_broadcast_structure(step_size, state)

  state = tf.nest.map_structure(tf.convert_to_tensor, state)
  momentum = tf.nest.map_structure(tf.convert_to_tensor, momentum)
  state = tf.nest.map_structure(tf.convert_to_tensor, state)

  if state_grads is None:
    _, _, state_grads = call_and_grads(target_log_prob_fn, state)
  else:
    state_grads = tf.nest.map_structure(tf.convert_to_tensor, state_grads)

  momentum = tf.nest.map_structure(lambda m, sg, s: m + 0.5 * sg * s, momentum,
                                   state_grads, step_size)

  kinetic_energy, kinetic_energy_extra, momentum_grads = call_and_grads(
      kinetic_energy_fn, momentum)

  state = tf.nest.map_structure(lambda x, mg, s: x