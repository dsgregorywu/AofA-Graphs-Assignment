# AofA-Graphs-Assignment

Name: Derec Gregory

Implementation: My implementation is pretty standard, for DFS everything is stack-based, where the algorithm searches for neighbors of a vertex using a get_neighbors helper function that I added and parses through them in reversed order to ensure that the vertices are being accessed in the correct order. My BFS algorithm is queue based, where it searches for any neighbors that haven't been visited and are not in the queue, visits all of them, then moves on to a deeper layer of searching. I didn't fully understand these algorithms before this project so I had to do some research on how they work, but I understand them both a lot better now!

Instructions: Running the program.py file should in theory bring up an option to start at a specific point. Type in a vertex name and from there it should run both search algorithms and return the other vertices in visited order. 

Since I wasn't incredibly familiar with either algorithm beforehand, any assumptions I made were researched beforehand to make sure I implemented it correctly.

DFS Traversal (starting at Salem):

Visiting: Salem
Visiting: Portland
Visiting: Astoria
Visiting: Seaside
Visiting: Tillamook
Visiting: Newport
Visiting: Corvallis
Visiting: Eugene
Visiting: Bend
Visiting: Redmond
Visiting: Madras
Visiting: The_Dalles
Visiting: Hood_River
Visiting: Pendleton
Visiting: Ontario
Visiting: Burns
Visiting: Crater_Lake
Visiting: Medford
Visiting: Roseburg
Visiting: Coos_Bay
Visiting: Florence
Visiting: Ashland

BFS Traversal (starting at Salem):

Visiting: Salem
Visiting: Portland
Visiting: Eugene
Visiting: Corvallis
Visiting: Astoria
Visiting: Hood_River
Visiting: Newport
Visiting: Bend
Visiting: Crater_Lake
Visiting: Roseburg
Visiting: Seaside
Visiting: The_Dalles
Visiting: Tillamook
Visiting: Florence
Visiting: Redmond
Visiting: Burns
Visiting: Medford
Visiting: Coos_Bay
Visiting: Pendleton
Visiting: Madras
Visiting: Ashland
Visiting: Ontario
