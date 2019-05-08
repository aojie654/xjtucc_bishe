tr0 = """
This is a text for test.
Need to replace: 123 234 345 456, 321 432 543 654
Replace to: 123, 321
"""

dct0 = {'123': ['123', '234', '345', '456'],
    '321': ['321', '432', '543', '654']}
dct0kl = list(dct0.keys())

print("B4:"+tr0)

# 使用t2遍历字典
for t2 in dct0kl:
    # 使用tt遍历字典的值
    dct0vl=list(dct0[t2])
    for t3 in range(1, len(dct0vl)):
        # 使用key替换values, 即人名替换别名
        tr0 = tr0.replace(dct0vl[t3], t2)

print("After:"+tr0)
