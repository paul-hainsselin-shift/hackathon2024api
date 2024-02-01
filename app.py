from flask import Flask, request, jsonify
import os
from azure.core.exceptions import AzureError
from azure.cosmos import CosmosClient, PartitionKey
from Graph import Graph, Node, Edge

app = Flask(__name__)

URI = 'https://team17.documents.azure.com:443/'
gremlin_endpoint = 'wss://team17.gremlin.cosmos.azure.com:443/'
auth_key = os.environ.get('primary_db_key')
auth_key = "f71da6Q1B8wOID71BIUiEzJMSyoTFpZxrDjTPJJsRszW3z3vIgCkQxHDs94wnMecR4g1XFoVw61NACDbRxXCEg=="

db_name = 'graphdb'
container_name = 'Network'

client = CosmosClient(URI, credential=auth_key)
database = client.get_database_client(db_name)
container = database.get_container_client(container_name)

# Endpoint to get a graph (simplified example)
@app.route('/GetGraph', methods=['GET'])
def get_graph():
    all_obj = list(container.query_items(
      query="SELECT * FROM c",
      enable_cross_partition_query=True
    ))

    edges = [x for x in all_obj if "_isEdge" in x]
    nodes = [x for x in all_obj if "_isEdge" not in x]

    my = Graph()

    for n in nodes:
        new_node = Node(id=n["id"], label=n["label"])
        my.add_node(new_node)

    for e in edges:
        node1 = my.get_node(e["_sink"])
        node2 = my.get_node(e["_vertexId"])
        new_edge = Edge(node1, node2, "red", e['id'])
        my.add_edge(new_edge)

    dd = my.to_dic()
    print(dd)
    return jsonify(dd)


# Endpoint to get the shortest path between two nodes
@app.route('/GetShortestPath', methods=['GET'])
def get_shortest_path():
    return jsonify(['2963', '2940'])




if __name__ == '__main__':
    app.run(debug=True)
