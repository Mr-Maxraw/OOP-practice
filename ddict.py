from collections import defaultdict

cnt = defaultdict(lambda : 0)
for i in "skvbdsfvk":
    cnt[i] += 1
print(cnt.items())