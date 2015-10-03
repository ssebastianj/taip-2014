# -*- coding: utf-8 -*-

def find_lists_numbers(lines):
    line_count_ids = [len(lines)]
    lines_qty = 0

    for i, number in enumerate(reversed(lines), start=1):
        if number == lines_qty:
            lines_qty = 0
            line_count_ids.append(len(lines) - i)
        else:
            lines_qty += 1

    return sorted(line_count_ids)
