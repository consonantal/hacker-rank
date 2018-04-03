N = int(raw_input())

students = list()
for _ in range(N):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print s

