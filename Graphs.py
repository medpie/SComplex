import networkx as nx
import matplotlib.pyplot as plt

def graphs(Scomplex):
  sc = nx.Graph()
  for i in range(len(Scomplex)):
    sc.add_node(i, label = i)
  for k in range(len(Scomplex)):
    for i in range(len(Scomplex[k])-1):
      for j in range(i+1, len(Scomplex[k])):
        sc.add_edge(Scomplex[k][i], Scomplex[k][j])
  plt.figure(figsize=(10,10))
  pos = nx.spring_layout(sc, k=1.6)
  nx.draw(sc, pos, node_color='yellow', node_size=500, edge_color='blue', with_labels = True)

  plt.show()

#Scomplex = [[2,3,5,4],[4,9]]
#graphs(Scomplex)

