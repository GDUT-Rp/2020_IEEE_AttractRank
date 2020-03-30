import numpy as np
import pandas as pd


def attractrank(od_matrix, distance_matrix, r=0.9):
    od_matrix = np.array(od_matrix)
    distance_matrix = np.array(distance_matrix)
    g_matrix = 1 / distance_matrix
    od_normalized = np.dot(np.diag([1 / i if i != 0 else i for i in od_matrix.sum(axis=1)]), od_matrix)
    g_normalized = np.dot(np.diag([1 / i for i in g_matrix.sum(axis=1)]), g_matrix)
    p_martix = np.dot(np.diag([1 - r if i != 0 else 1 for i in od_matrix.sum(axis=1)]), g_normalized) + od_normalized * r
    res = np.linalg.eig(p_martix.T)
    for idx, eigen in enumerate(res[0]):
        if abs(eigen - 1) < 1e-6:
            ar = res[1][:,idx]
            ar_normalized = ar / ar.sum()
            return ar_normalized * od_matrix.sum()
    return None


### test
od_hour = pd.read_csv('source.csv')
od = od_hour[(od_hour['date_month'] == 2) & (od_hour['date_day'] == 1) & (od_hour['date_hour'] == 9)]
num_district = 134
od_matrix = np.zeros([num_district] * 2)

for row in od.iterrows():
    row = row[1]
    od_matrix[row['from_idx'], row['to_idx']] = row['route_weight']

distance_matrix = pd.read_csv('distance_matrix.csv')
ar = attractrank(od_matrix, distance_matrix.iloc[:, 1:])
print(ar)
