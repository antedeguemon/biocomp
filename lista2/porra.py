import pprint

s1 = "aaat"
s2 = "gat"

w = -4 # gap penalty
def valor(a, b):
    if a == b: # match score
        return 5
    return -3 # mismatch score

m = len(s1)
n = len(s2)

scores = []
for i in range(m+1):
    scores.append([])
    for j in range(n+1):
        scores[i].append(0)

for i in range(0, m+1):
    scores[i][0] = w * i
for i in range(0, n+1):
    scores[0][i] = w * i



for i in range(1, m+1):
    for j in range(1, n+1):
        a = scores[i-1][j-1] + valor(s1[i-1], s2[j-1])
        b = scores[i-1][j] + w
        c = scores[i][j-1] + w
        scores[i][j] = max(a, b, c)


pprint.pprint(scores)
align1 = ''
align2 = ''
i, j = m, n
while i > 0 and j > 0:
    score_current = scores[i][j]
    score_diagonal = scores[i-1][j-1]
    score_up = scores[i][j-1]
    score_left = scores[i-1][j]

    if score_current == score_diagonal + valor(s1[i-1], s2[j-1]):
        align1 += s1[i-1]
        align2 += s2[j-1]
        i -= 1
        j -= 1
    elif score_current == score_left + w: # esquerda yi alinhado com espaco
        align1 += s1[i-1]
        align2 += '-'
        i -= 1
    elif score_current == score_up + w: # cima -> xi alinhado com espaco
        align1 += '-'
        align2 += s2[j-1]
        j -= 1

while i > 0:
    align1 += s1[i-1]
    i -= 1
    align2 += '-'
while j > 0:
    align1 += '-'
    align2 += s2[j-1]
    j -= 1
