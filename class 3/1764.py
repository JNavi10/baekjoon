import sys

input = sys.stdin.readline

unheard_count, unseen_count = map(int, input().split())

unheard_set = set()
answer_list = []
for _ in range(unheard_count):
    unheard_set.add(input().strip())

for _ in range(unseen_count):
    person = input().strip()
    if person in unheard_set:
        answer_list.append(person)

answer_list.sort()

print(len(answer_list))
print('\n'.join(answer_list))