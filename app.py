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
        new_edge = Edge(node1, node2, "red", 'id')
        my.add_edge(new_edge)

    dd = my.to_dic()
    print(dd)
    return jsonify(dd)


# Endpoint to get the shortest path between two nodes
@app.route('/GetShortestPath', methods=['POST'])
def get_shortest_path():
    data = request.json  # Get data from POST request body
    start_node = data.get('start')
    end_node = data.get('end')

    # Implement the logic to calculate the shortest path between `start_node` and `end_node`
    # This is placeholder logic
    path = f"Shortest path from {start_node} to {end_node}"

    return jsonify(
        {
          "nodes": [
            {
              "id": "AWS",
              "name": "AWS",
              "label": "1",
              "title": "AWS",
              "shape": "image",
              "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4qneFgROiufDyIrsXWpq_GhoQWnnxHuoclPljXeXgtlcGEParu75dPQ4TLafJeLJssXc&usqp=CAU",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "IBM",
              "color": "blue",
              "shape": "image",
              "label": "2",
              "title": "IBM",
              "image": "https://upload.wikimedia.org/wikipedia/commons/2/24/IBM_Cloud_logo.png",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "SQL",
              "color": "blue",
              "shape": "image",
              "title": "SQL",
              "label": "3",
              "image": "https://thumbs.dreamstime.com/b/sql-database-icon-logo-design-ui-ux-app-orange-inscription-shadow-96841969.jpg",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "S3",
              "color": "blue",
              "shape": "image",
              "title": "S3",
              "label": "4",
              "image": "https://sonraisecurity.com/wp-content/uploads/aws-s3-icon.png",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Azure",
              "color": "blue",
              "shape": "image",
              "label": "5",
              "title": "Azure",
              "image": "https://www.openbravo.com/blog/wp-content/uploads/2020/03/azure-cloud.jpg",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "MongoDB",
              "color": "blue",
              "shape": "image",
              "label": "6",
              "title": "MongoDB",
              "image": "https://cyclr.com/wp-content/uploads/2022/03/ext-553.png",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "ELB",
              "color": "purple",
              "shape": "image",
              "label": "7",
              "title": "ELB",
              "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZPd9rU5qaOuUmt2qwyBi6u_Xrn4PMV21SXNdHj2Me65OgDCStw4chydnmGa0-s1a7e_w&usqp=CAU",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Saas",
              "color": "purple",
              "shape": "image",
              "label": "8",
              "title": "Saas",
              "image": "https://ongoingwarehouse.com/Pictures/MicrosoftTeams-image.png",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Notion",
              "color": "purple",
              "shape": "image",
              "label": "9",
              "title": "Notion",
              "image": "https://cdn.icon-icons.com/icons2/2429/PNG/512/notion_logo_icon_147257.png",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Appengine",
              "label": "10",
              "color": "purple",
              "title": "Appengine",
              "shape": "image",
              "image": "https://www.howtogeek.com/wp-content/uploads/csit/2020/06/29add7ff.png?height=200p&trim=2,2,2,2",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Sematext",
              "label": "11",
              "color": "purple",
              "title": "Sematext",
              "shape": "image",
              "image": "https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_d6fa77d54b71a3a68842371d85aba442/sematext-cloud.jpg",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Jenkins",
              "label": "12",
              "color": "purple",
              "title": "Jenkins",
              "shape": "image",
              "image": "https://www.learntek.org/blog/wp-content/uploads/2018/05/jenkins_image.png",
              "size": 20,
              "cost": "$1000"
            },
            {
              "id": "Githup",
              "label": "13",
              "color": "purple",
              "title": "Githup",
              "shape": "image",
              "image": "https://foundations.projectpythia.org/_images/GitHub-logo.png",
              "size": 20,
              "cost": "$1000"
            }
          ],
          "edges": [
            {
              "from": "AWS",
              "to": "IBM",
              "color": "red",
              "id": "59c01ad8-e289-4dd7-b097-25f1732ce35a"
            },
            {
              "from": "AWS",
              "to": "SQL",
              "color": "red",
              "id": "2801c851-9da5-46d5-a407-29338483bd97"
            },
            {
              "from": "IBM",
              "to": "S3",
              "color": "red",
              "id": "42d8b390-d8b1-4e0b-9b0f-15d1c9061454"
            },
            {
              "from": "IBM",
              "to": "Azure",
              "color": "red",
              "id": "d1d2ee89-5561-46e1-b7cf-2565cef879ed"
            },
            {
              "from": "IBM",
              "to": "MongoDB",
              "color": "red",
              "id": "4dfe430d-9d6f-46ca-944b-7c1f9f11fdab"
            },
            {
              "from": "MongoDB",
              "to": "AWS",
              "color": "red",
              "id": "94b3d3c3-6a6c-4073-bb39-0811a8107e4e"
            },
            {
              "from": "Azure",
              "to": "MongoDB",
              "color": "red",
              "id": "bee3ad13-9157-40ba-a0c1-13998ad34164"
            },
            {
              "from": "MongoDB",
              "to": "ELB",
              "color": "red",
              "id": "93565a85-ab81-47b3-b01e-bf72fc8a074c"
            },
            {
              "from": "AWS",
              "to": "ELB",
              "color": "purple",
              "id": "f32f3342-2d61-4a06-ad1e-3bec82584217"
            },
            {
              "from": "ELB",
              "to": "Saas",
              "color": "purple",
              "id": "69c9532b-0aaa-4033-8eee-d13d7860bbc6"
            },
            {
              "from": "Saas",
              "to": "Notion",
              "color": "purple",
              "id": "f8486ad7-c6b9-4745-b453-43bfcd47a262"
            },
            {
              "from": "Notion",
              "to": "Appengine",
              "color": "purple",
              "id": "ac67731e-f471-4af1-a55b-cbf5eb8ae66c"
            },
            {
              "from": "Githup",
              "to": "Jenkins",
              "color": "purple",
              "id": "9fd11cc1-d7c7-4ab5-96e1-379e51633d96"
            },
            {
              "from": "Sematext",
              "to": "Appengine",
              "color": "purple",
              "id": "180cad79-b0b9-4250-b679-dfe98cb0082c"
            },
            {
              "from": "Githup",
              "to": "Sematext",
              "color": "purple",
              "id": "2681d6e6-01e0-4e57-a719-b7cf0dfc66e6"
            },
            {
              "from": "Sematext",
              "to": "AWS",
              "color": "purple",
              "id": "9ce9b19b-beb5-435c-90c8-8071d35a4536"
            },
            {
              "from": "Jenkins",
              "to": "ELB",
              "color": "purple",
              "id": "75373f24-23b6-4695-95af-46b8567cd661"
            }
          ]
        })


if __name__ == '__main__':
    app.run(debug=True)
