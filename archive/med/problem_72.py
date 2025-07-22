word1 = "plasma"
# word1 = "a"
word2 = "altruism"
# word2 = "ab"

matches = []
matches_count = 0
counter = 0
for i in range(0, len(word2)):
    char1 = word2[i]
    for j in range(0, len(word1)):
        char2 = word1[j]

        if char1 == char2:
            if matches_count > 0:
                last_match = matches[matches_count - 1]
                if j <= last_match[0]:
                    if i == j: matches[matches_count - 1] = [j, i, char1]
                    continue

            matches.append([j, i, char1])
            matches_count += 1
            break

word1len = len(word1)
matchcount = len(matches)
moves = 0
print(matches)
for i, match in enumerate(matches):
    word1_idx = match[0]
    word2_idx = match[1]

    kurang = word2_idx - word1_idx
    panjang_kurang = abs(word1len - len(word2))
    if kurang == 0: continue
    print(i, kurang, panjang_kurang)
    if abs(kurang - panjang_kurang) == 1:
        moves += abs(kurang)
        if word1len != len(word2):
            if kurang > 0: matches_count += 1
            word1len += kurang
        for j in range(i, len(matches)):
            matches[j][0] += kurang
    else:
        matches_count -= 1
    print(i, matches)

print(matches_count, word1len, len(word2), moves)
extra = abs(word1len - len(word2)) if word1len < len(word2) else 0
print(abs(matches_count - word1len) + moves + extra)
# matchcount = matchcount + abs(abs(word1len - moves) - len(word2))
# print(matchcount)
# moves = moves + abs(abs(word1len - moves) - len(word2))
# print(moves)
# moves = moves + abs(matchcount - len(word2))
# print(moves)
