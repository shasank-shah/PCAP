def shortcut( s ):
    result_string = ''
    for ch in s:
        if ch in 'aeiouAEIOU':
            ch = ''
        result_string += ch
    return result_string

print(shortcut("Shasank SHAH"))