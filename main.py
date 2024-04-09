import utils
import ranks

# ranks.solve('AB+BC', utils.set_strings_from_minimal_sets([
#     '110',
#     '011',
# ]), 'ABC', 2, 5, int(1e9 + 7))

# ranks.solve('1/AB & 1/CD', utils.set_strings_from_thresholds(4, [
#     (1, [0, 1]),
#     (1, [2, 3]),
# ]), 'ABCD', 2, 5, int(1e9 + 7))

# ranks.solve('3/ABCDE', utils.set_strings_from_thresholds(5, [
#     (3, [0, 1, 2, 3, 4]),
# ]), 'ABCDE', 3, 5, int(1e9 + 7))

# ranks.solve('1/AB & 1/CDE & 3/ABCDE', utils.set_strings_from_thresholds(5, [
#     (1, [0, 1]),
#     (1, [2, 3, 4]),
#     (3, [0, 1, 2, 3, 4]),
# ]), 'ABCDE', 5, 5, int(1e9 + 7))

ranks.solve('AB+AC+CD', utils.set_strings_from_minimal_sets([
    '1100',
    '1010',
    '0011',
]), 'ABCD', 5, 5, int(1e9 + 7))
