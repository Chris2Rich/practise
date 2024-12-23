data = [2, 3, 1, 1, 4, 1, 2, 4, 1]
scores = [5, 3, 6, 6]

#convert every element to three tuple, score, first, index
data = [(data[i], scores[data[i] - 1]) for i in range(0, len(data))]
#O(n) scan to turn into tuple for easy manip

x = 0 #max
mset = set() #set of movies seen
scoreset = set() #set of scores (removes risk of repeated subtractions)

#update score only when adding/removing from set, avoids O(n) recalculation
print(data)