#Breadth-first search, Python
from collections import deque
from graph import constructGraph


def bfsearch(root, vertex):
	queue = deque([root])
	visitedNodes = set()

	#keep looking while queue is not empty
	while len(queue) > 0:
		node = queue.pop()
		
		#if node is visited, go to the next node in graph
		if node in visitedNodes:

			continue

		#else add node to visitedNodes list and check if it is found
		else:
			print node.value, "->",
			visitedNodes.add(node)
			if node.value == vertex:
				return True

			for x in node.adjacentNodes:
				if x not in visitedNodes:
					queue.append(x)

	return False


if __name__ == "__main__":
   vertices = ["s", "x", "a", "z", "c", "d","f","v"]
   edges = [("s","x"), ("s","a"), ("a","z"), ("x","d"), ("x","c"), ("d","f"),("c","v"),("f","v")]



   G = constructGraph(vertices, edges)

   print bfsearch(G, "e")
   print bfsearch(G, "v")
