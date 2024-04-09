import numpy
import galois

def solve(formula, set_strings, labels_string, column_count, max_value, modulo):
    label_count = len(set_strings[0][0])
    labels = [ord(char) - ord('A') for char in labels_string]
    shape = len(labels_string), column_count
    objective = [1] * shape[1]

    def backtrack(i, j):
        if i == shape[0]:
            print(formula)
            print(matrix)
            exit(0)
        if j == shape[1]:
            for submatrix_row_ids_mask in range(1 << i):
                if is_bad_submatrix(submatrix_row_ids_mask ^ (1 << i)):
                    return
            backtrack(i + 1, 0)
            return
        for value in range(max_value):
            matrix[i][j] = value
            backtrack(i, j + 1)

    def is_bad_submatrix(submatrix_row_ids_mask):
        submatrix_row_ids = [row_id for row_id in range(shape[0]) if submatrix_row_ids_mask & (1 << row_id) != 0]
        submatrix_labels = [labels[row_id] for row_id in submatrix_row_ids]
        set_string = ''.join('1' if label in submatrix_labels else '0' for label in range(label_count))
        if set_string in set_strings[1]:
            return False
        is_accepted_set = set_string in set_strings[0]
        full_submatrix_length = len([row_id for row_id in range(shape[0]) if labels[row_id] in submatrix_labels])
        is_full_submatrix = len(submatrix_row_ids) == full_submatrix_length
        submatrix = [matrix[row_id] for row_id in submatrix_row_ids]
        gf = galois.GF(modulo)
        does_contain_objective = numpy.linalg.matrix_rank(gf(submatrix)) == numpy.linalg.matrix_rank(gf(submatrix + [objective]))
        return is_accepted_set and is_full_submatrix and not does_contain_objective or not is_accepted_set and does_contain_objective

    matrix = [[0] * shape[1] for _ in range(shape[0])]
    backtrack(0, 0)
