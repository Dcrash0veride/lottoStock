import random
from collections import Counter

total_white_balls = []
total_power_balls = []
total_power_plays = []
with open(r'C:\Users\dcrash0veride\Documents\lottery.txt', 'r') as numbers:
    for line in numbers:
        splits = line.split()
        date = splits[0]
        white_balls = ''.join(splits[1:6])
        power_ball = splits[6]
        power_play = splits[7]
        total_white_balls.append(white_balls)
        total_power_balls.append(power_ball)
        total_power_plays.append(power_play)

each_ball = []
for ball in total_white_balls:
    individual = ball.split(',')
    each_ball.append(individual)

each_power_ball = []
for pball in total_power_balls:
    pwrball = pball.split(',')
    if any(int(x) <= 26 for x in pwrball):
        each_power_ball.append(pwrball)
    else:
        pass

each_power_play = []
for pplay in total_power_plays:
    ppball = pplay.split(',')
    each_power_play.append(ppball)

last_sixty9_balls = each_ball[-14:]

possible_balls = []

for number in range(1, 70):
    possible_balls.append(f'{number:02}')

most_common_power_play = Counter(ppnum for ppnums in each_power_play for ppnum in ppnums).most_common(1)
least_common_power_play = Counter(ppnum for ppnums in each_power_play for ppnum in ppnums).most_common()[: -1-1:-1]
most_common_power_ball = Counter(pnum for pnums in each_power_ball for pnum in pnums).most_common(1)
least_common_power_ball = Counter(pnum for pnums in each_power_ball for pnum in pnums).most_common()[: -1-1:-1]
most_common = Counter(num for nums in each_ball for num in nums).most_common(5)
least_common = Counter(num for nums in each_ball for num in nums).most_common()[: -5-1:-1]

probability_counter = Counter(bbnum for bbnums in last_sixty9_balls for bbnum in bbnums)

balls_called = []

for probability in probability_counter:
    balls_called.append(probability.split(':'))

cleaned_most_common = [eb[0] for eb in most_common]
cleaned_least_common = [eb[0] for eb in least_common]
cleaned_most_common_power_play = [ex[0] for ex in most_common_power_play]
cleaned_least_common_power_play = [ex[0] for ex in least_common_power_play]
cleaned_most_common_power_ball = [ea[0] for ea in most_common_power_ball]
cleaned_least_common_power_ball = [ea[0] for ea in least_common_power_ball]

called_soon = []

loop_counter = 0

bare_balls_lol = []

for i in balls_called:
    bare_balls_lol.append(balls_called[loop_counter][0])
    loop_counter += 1

for i in possible_balls:
    if i not in bare_balls_lol:
        called_soon.append(i)

def generate_random_games():
    fun_game = random.sample(called_soon, 5)
    print(fun_game)
    for i in fun_game:
        called_soon.remove(i)
    if len(called_soon) > 5:
        generate_random_games()




print("Your lucky numbers are:")
print(str(cleaned_most_common) + " " + str(cleaned_most_common_power_ball) + " " + str(cleaned_most_common_power_play))
print("\n")
print("The unlucky numbers are:")
print(str(cleaned_least_common) + " " + str(cleaned_least_common_power_ball) + " " + str(cleaned_least_common_power_play))
print("Random games are:")
generate_random_games()