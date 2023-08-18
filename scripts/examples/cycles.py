import networkx as nx
import matplotlib.pyplot as plt


names = [
    'The Cantos',
    'Zukowsky',
    'Eliot',
    'Yeats',
    'Dante',
    'Cavalcanti',
]

edges = []
for name in names:
    if name == 'The Cantos':
        continue
    edges = edges + [('The Cantos', name)]

edges = edges + [
    ('Zukowsky', 'The Cantos'),
    ('Eliot', 'The Cantos'),
    ('Yeats', 'The Cantos'),
    ('Cavalcanti', 'Dante'),
    ('Dante', 'Cavalcanti'),
]


G = nx.Graph()
G.add_nodes_from(names)
G.add_edges_from(edges)

# graph 3, seed 111
# graph 4, seed 10
pos = nx.spring_layout(G, seed=10)

fig, ax = plt.subplots()

# nodes and labels
nx.draw_networkx_nodes(G, pos, ax=ax, node_color='white', node_size=3000)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=8)

# edges
arc_rad = 0.25
curved_edges = [edge for edge in edges if tuple(reversed(edge)) in edges]
straight_edges = list(set(G.edges()) - set(curved_edges))
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges, edge_color='white')
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}', arrows=True, edge_color='white')

ax.set_facecolor('black')
fig.set_facecolor('black')

plt.show()
