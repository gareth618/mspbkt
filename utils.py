def includes(set_string1, set_string2):
    return not any(bit2 == '1' and bit1 == '0' for bit1, bit2 in zip(set_string1, set_string2))

def minterms_first(set_strings):
    minterms = []
    non_minterms = []
    for set_string in set_strings:
        if any(includes(set_string, set_string_small) for set_string_small in minterms):
            non_minterms += [set_string]
        else:
            minterms += [set_string]
    return minterms, non_minterms

def set_strings_from_thresholds(label_count, thresholds):
    set_strings = []
    for set_mask in range(1 << label_count):
        set_string = ''.join('1' if set_mask & (1 << label) else '0' for label in range(label_count))
        valid_set = True
        for threshold, labels in thresholds:
            if sum(int(set_string[label] == '1') for label in labels) < threshold:
                valid_set = False
                break
        if valid_set:
            set_strings += [set_string]
    return minterms_first(set_strings)

def set_strings_from_minimal_sets(minimal_set_strings):
    label_count = len(minimal_set_strings[0])
    set_strings = []
    for set_mask in range(1 << label_count):
        set_string = ''.join('1' if set_mask & (1 << label) else '0' for label in range(label_count))
        for minimal_set_string in minimal_set_strings:
            if all(minimal_set_string[label] <= set_string[label] for label in range(label_count)):
                set_strings += [set_string]
                break
    return minterms_first(set_strings)
