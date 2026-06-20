"""
longest substring
"""

s = "abcabcbb"
l = len(s)
max_len = 0
for i in range(l):
    for j in range(i,l):
        sub_str = s[i:j+1]

        if len(sub_str) == len(set(sub_str)):
            max_len = max(max_len, len(sub_str))

print(max_len)
