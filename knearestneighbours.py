'''
calculate distance from the query point to every training point
sort them from smallest distance to biggest
take the first k closest points
check their labels
whichever label appears most is the prediction
'''

data = [
    ([1, 1], "Red"),
    ([2, 1], "Red"),
    ([2, 2], "Red"),
    ([6, 6], "Blue"),
    ([7, 6], "Blue"),
    ([6, 7], "Blue")
]
query = [3, 2]
k = 3

def euc_dist(point1,point2):
    distance = 0

    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance

def distance_lister(data,query):
    distances_to_all_points = []

    for i in range(len(data)):
        point = data[i][0]
        label = data[i][1]
        dist = euc_dist(point,query)
        distances_to_all_points.append((dist,label))
    return distances_to_all_points

def list_to_dict(data):
    freq = {}

    for label in data:
        if label in freq:
            freq[label] += 1
        else:
            freq[label] = 1
    return freq

def most_freq_label(data):
    workable = list_to_dict(data)
    max_count = 0
    max_label = ''

    for label in workable:
        if workable[label] > max_count:
            max_count = workable[label]
            max_label = label
    return max_label

def take_k_points(data,query,k):
    all_distances = sorted(distance_lister(data, query))
    return all_distances[:k]


print(most_freq_label(take_k_points(data,query,k))[1])
