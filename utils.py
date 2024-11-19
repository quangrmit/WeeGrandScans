def decide_attr(val1, val2):
    empty_values = [None]
    if val1  in empty_values:
        if val2 in empty_values:
            return val1
        return val2
    if val2 in empty_values:
        return val1
    # If both are not in empty values
    if isinstance(val1, (float, int)):
        return val1
    else:
        return val1 if len(val1) >= len(val2) else val2
