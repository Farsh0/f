from functools import reduce

sentences = ['научиться плести рыболовные сети',
             'обучать нейронные сети',
             'паук ловит в сети мух']

podch = reduce(lambda a, x: a + x.count('сети'), sentences, 0)

print(podch)
