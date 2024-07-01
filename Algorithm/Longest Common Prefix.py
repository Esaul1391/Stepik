strs = ["dog","racecar","car"]

min_value = min(strs)
for i, value in enumerate(min_value):
    check = all(k[i] == value for k in strs)
    if not check:
        i_ = min_value[:i]
        res = i_ if len(i_) > 0 else ''
        
        break

# O(N * M)