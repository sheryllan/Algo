

def replace(s: str) -> str:
    num_str = 'number'
    chars = []
    found_num = False

    for c in s:
        if c.isdigit():
            found_num = True
        else:
            if found_num:
                chars.append(num_str)
            chars.append(c)
            found_num = False

    if found_num:
        chars.append(num_str)

    return ''.join(chars)



assert replace("a1b2c3") == "anumberbnumbercnumber"
assert replace("a1b2jfei4885c3") == "anumberbnumberjfeinumbercnumber"
