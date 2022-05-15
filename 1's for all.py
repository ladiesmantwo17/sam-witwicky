n = list(map(int, input()))
cnt = 0
cnt_with0 = 0
cnt_0 = 0
cnt_0_list = []
cnt_constants = []
if 0 in n:
    for j in range(len(n)):
        a = n[j]
        if a == 0:
            cnt_0 += 1
        else:
            cnt_constants.append(a)
            cnt_0_list.append(cnt_0)
            cnt_0 = 0
    cnt_0_list.append(cnt_0)

    for i in range(len(cnt_0_list) - 1):
        cnt_with0 += 7 * cnt_0_list[i + 1]

    for i in range(len(cnt_constants)):
        if cnt_constants[i] == 9:
            cnt_with0 += 6
        elif cnt_constants[i] == 6:
            cnt_with0 += 5
        elif cnt_constants[i] == 4:
            cnt_with0 += 4
        elif cnt_constants[i] == 8:
            cnt_with0 += 6
        elif cnt_constants[i] == 1:
            if cnt_0_list[i + 1] == 0:
                cnt_with0 += 1
            else:
                None
        else:
            cnt_with0 += cnt_constants[i]


if 0 not in n:
    for i in range(len(n)):
        if n[i] == 9:
            cnt = cnt + 6
        elif n[i] == 6:
            cnt = cnt + 5
        elif n[i] == 4:
            cnt = cnt + 4
        elif n[i] == 8:
            cnt = cnt + 6
        else:
            cnt = cnt + n[i]
# print(cnt)
# print(cnt_with0)
# print(cnt_0)
# print(cnt_0_list)
# print(cnt_constants)
print(cnt + cnt_with0)