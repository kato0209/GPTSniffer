`
        as it is not a `Tensor` or Python `list`.
      previous_kernel_results: `Tensor` or Python `list` of `Tensor`s
        representing the previous state(s) of the Markov chain(s),
        _after_ application of `bijector.forward`. The first `r`
        dimensions index independent chains,
        `r = tf.rank(target_log_prob_fn(*previous_state))`. The
        `inner_kernel.one_step` does not actually use `previous_state`
        as it is not a `Tensor` or Python `list