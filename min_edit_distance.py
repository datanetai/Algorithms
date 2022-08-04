#minimum edit distance
def min_edit_dist(s1, s2):
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[-1] == s2[-1]:
        return min_edit_dist(s1[:-1], s2[:-1])
    return 1 + min(min_edit_dist(s1, s2[:-1]), min_edit_dist(s1[:-1], s2))

print(min_edit_dist("sunday", "saturday"))