
    if expected_type =='string':
        try:
            if isinstance(value, basestring):
                return value
        except Exception:
            raise TypeError('%s is not a string' % key)
    elif expected_type == 'int':
        try:
            if isinstance(value, int):
                return value
        except