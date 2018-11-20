import random
import numpy as np

class KMeans:
	def __init__(self, means=2):
		self.means = means
		self.points = []
		self.clusters = None
		self.predictions = {}

	def num_axis(self):
		return len(self.points[0])

	def add_point(self, point):
		self.points.append(point)

	def get_median(self, axis):
		total = 0
		for point in self.points:
			total += point[axis]
		return total/len(self.points)

	def get_max_min(self, axis):
		# get max and min from an axis
		min_point, max_point = None, None
		for point in self.points:
			if min_point is None or min_point > point[axis]:
				min_point = point[axis]
			if max_point is None or max_point < point[axis]:
				max_point = point[axis]
		return min_point, max_point

	def dist(self, a, b):
		return np.linalg.norm(np.array(a) - np.array(b), axis=0)

	def random_point(self):
		# passes arround all axis getting random numbers (along with max and min)
		point = []
		for axis in range(self.num_axis()):
			min_point, max_point = self.get_max_min(axis)
			point.append(random.uniform(min_point, max_point))
		return point

	def generate_first(self):
		if self.clusters is None:
			self.clusters = []
			for mean in range(self.means):
				self.clusters.append(self.random_point())
		self.predictions = {}
		for i in range(len(self.points)):
			point = self.points[i]
			min_dist, min_cluster = None, None
			for j in range(len(self.clusters)):
				cluster = self.clusters[j]
				dist = self.dist(point, cluster)
				if min_dist is None or min_dist > dist:
					min_dist = dist
					min_cluster = j
			try:
				self.predictions[min_cluster].append(i)
			except:
				self.predictions[min_cluster] = []
				self.predictions[min_cluster].append(i)
			#print "Min cluster to ", point, ":", min_cluster

	def generate(self):
		print "Generating..."
		# update clusters to median of its people based on last predictions
		for axis in range(self.num_axis()):
			for cluster in range(len(self.clusters)):
				points = self.predictions[cluster] # dando erro aqui....
				total = 0
				for point in points:
					total += self.points[point][axis]
				self.clusters[cluster][axis] = total / len(points)

		# updates predictions
		self.generate_first()
"""
means = KMeans(2)
means.add_point([1, 1])
means.add_point([2, 1])
means.add_point([8, 10])
means.add_point([9, 10])
means.generate_first()
print means.clusters
means.generate()
print means.clusters
means.generate()
print means.clusters
means.generate()
print means.clusters
"""
