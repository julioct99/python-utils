def nth_line(file, n):
    with open(file) as f:
        for i, line in enumerate(f):
            if i + 1 == n:
                return line


def similarity(file1, file2):
    total_lines, equal_lines = 0, 0
    with open(file1) as f:
        for i, line in enumerate(f):
            total_lines += 1
            if line == nth_line(file2, i + 1):
                equal_lines += 1
    return round(equal_lines / total_lines * 100, 2)
