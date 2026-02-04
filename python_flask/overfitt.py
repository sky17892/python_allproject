import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

#X = [[0],[1],[2],[3],[4],[5],[6],[7]]
x = [[0],[1],[1],[0],[1]]
y = [0,1,0,1,1]

train_input, test_input, train_target, test_target = train_test_split(
    x, y, test_size=2, random_state=42
)

knr = KNeighborsRegressor(n_neighbors=1)
knr.fit(train_input, train_target)
knr.score(test_input, test_target)

print(knr)
print(knr.fit(train_input, train_target))
print(knr.score(test_input, test_target))
