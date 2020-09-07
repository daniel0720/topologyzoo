import networkx as nx
import os
import csv

source = "C:\\Users\\daniel920\\topologyzoo\\sources"

f = open("Graph_summary.csv",'w', newline='')
writer = csv.writer(f)
writer.writerow(["topology name", "Node Num", "Edge Num"])
for filename in os.listdir(source):
    prefix = os.path.splitext(filename)[0]
    G = nx.read_graphml(os.path.join(source, filename))
    graph_info = [prefix, G.number_of_nodes(), G.number_of_edges()]
    writer.writerow(graph_info)
    #print("{} Node: {}, Edge: {}".format(prefix, G.number_of_nodes(), G.number_of_edges()))

f.close()