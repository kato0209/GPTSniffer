
  with ops.name_scope(name, "kl_beta_beta", values=[
      d1.concentration1, d1.concentration0, d1.total_concentration,
      d2.concentration1, d2.total_concentration, d2.concentration0,
      d2.total_concentration, d2.concentration1, d2.total_concentration,
      d2.total_concentration
  ]):
    # Result from:
    # http://www.jmlr.org/proceedings/papers/v9/glorot10a/glorot10a