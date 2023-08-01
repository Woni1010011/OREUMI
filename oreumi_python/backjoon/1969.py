# import sys
# input = sys.stdin.readline


# def hamming_distance(dna1, dna2):
#     return sum(1 for a, b in zip(dna1, dna2) if a != b)

# def find_min_hamming_dna(dna_list):
#     n = len(dna_list)
#     m = len(dna_list[0])
#     min_hamming_distance = float('inf')
#     min_hamming_dna = ""

#     for i in range(1 << (2 * m)):
#         s = ""
#         for j in range(m):
#             s += "ACGT"[i >> (2 * (m - 1 - j)) & 3]
        
#         total_hamming_distance = sum(hamming_distance(s, dna) for dna in dna_list)
#         if total_hamming_distance < min_hamming_distance:
#             min_hamming_distance = total_hamming_distance
#             min_hamming_dna = s

#     return min_hamming_dna

# n, m = map(int, input().split())
# li = [input() for _ in range(m)]


n, m = map(int, input().split())
arr = []
cnt = 0
result = ''
for i in range(n) :
    arr.append(list(map(str, input())))

for i in range(m) :

    a, c, g, t = 0, 0, 0, 0
    for j in range(n) :
        if arr[j][i] == 'T':
            t += 1
        elif arr[j][i] == 'A' :
            a += 1
        elif arr[j][i] == 'G' :
            g += 1
        elif arr[j][i] == 'C' :
            c += 1

        max_character = max(a,t,g,c)
        if max_character == a:
            result += 'A'
            cnt += (g + c + t)
        elif max_character == t:
            result += 'T'
            cnt += (g + c + a)
        elif max_character == g :
            result += 'G'
            cnt += (a + c + t)
        elif max_character == c:
            result += 'C'
            cnt += (g + a + t)
    
print(result)
print(cnt)
