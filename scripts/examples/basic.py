import networkx as nx
import matplotlib.pyplot as plt


names = [
    'The Cantos',
    'Homer',
    'Ovid',
    'Dante',
    'Sordello',
    'Sigismundo',
    'H.C. Douglas',
]

edges = []
for name in names:
    if name == 'The Cantos':
        continue
    edges = edges + [('The Cantos', name)]

edges = edges + [
    ('Homer', 'Dante'),
    ('Ovid', 'Dante'),
    # ('Sordello', 'Dante')
]

G = nx.Graph()
G.add_nodes_from(names)
G.add_edges_from(edges)


fig, ax = plt.subplots()

pos = nx.spring_layout(
    G,
)

nx.draw(
    G,
    with_labels=True,
    node_color='white',
    edge_color='white',
    node_size=3000,
    font_size=8,
    pos=pos
)

fig.set_facecolor('black')

plt.show()
