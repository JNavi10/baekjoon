N = int(input())

set_word = set()

for _ in range(N):
    set_word.add(input())

li = [[] for _ in range(50)]

while set_word:
    word = set_word.pop()
    li[len(word)-1].append(word)

for sub_li in li:
    for word in sorted(sub_li): 
        print(word)