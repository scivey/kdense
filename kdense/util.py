
def binsearch_closest(x, sorted_data, start_idx=None, end_idx=None):
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(sorted_data)
    if sorted_data[start_idx] > x:
        return start_idx, sorted_data[start_idx]
    if sorted_data[end_idx-1] < x:
        return end_idx-1, sorted_data[end_idx-1]

    section_len = end_idx - start_idx
    assert section_len > 0
    if section_len == 1:
        return start_idx, sorted_data[start_idx]
    elif section_len < 5:
        min_diff = abs(x - sorted_data[start_idx])
        min_idx = start_idx
        for idx in xrange(start_idx, end_idx):
            diff = abs(x - sorted_data[idx])
            if diff < min_diff:
                min_diff = diff
                min_idx = idx
        return min_idx, sorted_data[min_idx]
    else:
        mid_idx = start_idx + (section_len / 2)
        mid_val = sorted_data[mid_idx]
        if mid_val == x:
            return mid_idx, mid_val
        else:
            if mid_val < x:
                return binsearch_closest(x, sorted_data, start_idx=mid_idx, end_idx=end_idx)
            else:
                return binsearch_closest(x, sorted_data, start_idx=start_idx, end_idx=mid_idx)
