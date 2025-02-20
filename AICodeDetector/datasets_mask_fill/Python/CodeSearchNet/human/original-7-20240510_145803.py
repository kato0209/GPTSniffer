
  with tf.name_scope(name or "kl_half_normal_half_normal"):
    # Consistent with
    # http://www.mast.queensu.ca/~communications/Papers/gil-msc11.pdf, page 119
    return (tf.math.log(b.scale) - tf.math.log(a.scale) +
            (a.scale**2 - b.scale**2) / (2 * b.scale**2))