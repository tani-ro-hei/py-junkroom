# sort(ed) のお勉強

# (from functools.py)
def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        __hash__ = None
    return K

def comper(a, b):
    return -1 if len(a) < len(b) \
    else    1 if len(a) > len(b) \
    else   -1 if a < b \
    else    1 if a > b \
    else    0


with open('rand_entries1.txt') as f:
    lines1 = f.read().splitlines()
with open('rand_entries2.txt') as f:
    lines2 = f.read().splitlines()

# 辞書式:
lis1α = list(sorted(lines1))
lis2α = list(sorted(lines2))
# 1 or A の数 降順:
lis1β = list(sorted(lines1, key=lambda s: s.count('1'), reverse=True))
lis2β = list(sorted(lines2, key=lambda s: s.count('A'), reverse=True))
# 長さ→辞書式:
lis1γ = list(sorted(lines1, key=cmp_to_key(comper)))
lis2γ = list(sorted(lines2, key=cmp_to_key(comper)))
# 同じ(タプルで):
lis1δ = list(sorted(lines1, key=lambda s: (len(s), s)))
lis2δ = list(sorted(lines2, key=lambda s: (len(s), s)))

print(
    "辞書式:         ",
    "1の数 降順:     ",
    "長さ→辞書式:   ",
    "同じ(タプルで): ", '  ',

    "辞書式:         ",
    "Aの数 降順:     ",
    "長さ→辞書式:   ",
    "同じ(タプルで): ", '  ',
    sep=''
)
for i in range(0, 99):
    print(
        lis1α[i].ljust(16),
        lis1β[i].ljust(16),
        lis1γ[i].ljust(16),
        lis1δ[i].ljust(16), '  ',

        lis2α[i].ljust(16),
        lis2β[i].ljust(16),
        lis2γ[i].ljust(16),
        lis2δ[i].ljust(16), '  ',
        sep=''
    )
