inputEjemplo = "389125467"
inputMahatma = "952438716"
inputDiana = "327465189"

input = []
for num in inputDiana:
    input.append(int(num))

n = 1000000
moves = 10000000

cups = [None] * (n + 1)

maxCup = max(input)

for i in range(len(input) - 1):
    cups[input[i]] = input[i + 1]
cups[input[-1]] = maxCup + 1

for i in range(maxCup + 1, n):
    cups[i] = i + 1
cups[n] = input[0]

label = input[0]

for i in range(moves):
    pickedUp = [cups[label]]
    for _ in range(2):
        pickedUp.append(cups[pickedUp[-1]])
    cups[label] = cups[pickedUp[-1]]
    destination = label - 1
    while destination in pickedUp or destination == 0:
        destination -= 1
        if destination < 1:
            destination = n
    cups[pickedUp[-1]] = cups[destination]
    cups[destination] = pickedUp[0]
    label = cups[label]

a = cups[1]
b = cups[a]
print(a, b)
print(a * b)
