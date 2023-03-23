#Collatz Conjecture Graph Vizualization

import networkx as nx
import matplotlib.pyplot as plt

# User Input
n = int(input("Enter the starting number: "))

# Create graph
G = nx.DiGraph()

# First number a node
G.add_node(n)

# Apply the Collatz Conjecture until n reaches 1
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
        
    # Add the next number as a new node and connect it to the previous node 
    G.add_node(n)
    G.add_edge(n // 2 if n % 2 == 0 else (3 * n + 1) // 2, n)
    G.nodes[n]['pos'] = (-1, n) if n % 2 == 0 else (1, n) # if the node is even, -1 and odd 1
    
# Draw the graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True)
plt.show()





    
    










 