
        converted_row = []
        for col_name, col_val in zip(schema, row):
            if type(col_val) in (datetime, date):
                col_val = time.mktime(col_val.timetuple())
            elif isinstance(col_val, Decimal):
                col_val = float(col_val)
            elif col_type_dict.get(col_name) == "BYTES":
                col_val = base64.standard_b64encode(col_val).decode('ascii')
     