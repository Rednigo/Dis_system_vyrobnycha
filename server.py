import json
from flask import Flask, request
import Client
import ControlNode
import DataNode

app = Flask(__name__)

@app.route('/writemessage', methods=['POST'])
def write_message(Client, message):
    request.post(Client.write(json.dumps(message)))

@app.route('/<adress>/writemessage', methods=['POST'])
def write_messagenode(adress, DataNode, message):
    request.post(DataNode.write(json.dumps(message)))
@app.route('/getmessage', methods=['GET'])
def get_message(Client):
     request.get(Client.read())
@app.route('/<adress>/getmessage', methods=['GET'])
def get_messagenode(adress, DataNode):
     request.get(DataNode.read())
@app.route('/<adress>/addnode', methods=['POST'])
def add_node(adress, ControlNode, message):
     request.post(ControlNode.add_node(json.dumps(message)))

@app.route('/<adress>/removenode', methods=['POST'])
def remove_node(adress, ControlNode, message):
    request.post(ControlNode.remove_node(json.dumps(message)))

@app.route('/<adress>/getstats')
def get_stats(adress):
    return ControlNode.get_stats()

@app.route('/')
def index():
    return "Hello!"

#Щоб запустити прописати в консолі: flask --app server run --host=0.0.0.0
if __name__ == "__main__":
    app.run()

# class Handler(server.BaseHTTPRequestHandler):
#     def do_POST(self):
#         self.send_response(200)
#         self.end_headers()
#         body_length = int(self.headers['content-length'])
#         request_body_json_string = self.rfile.read(body_length).decode('utf-8')
#
#         # Printing  some info to the server console
#         print('Server on port ' + str(self.server.server_port) + ' - request body: ' + request_body_json_string)
#
#         json_data_obj = json.loads(request_body_json_string)
#         json_data_obj['SEEN_BY_THE_SERVER'] = 'Yes'
#
#         # Sending data to the Client
#         self.wfile.write(bytes(json.dumps(json_data_obj), 'utf-8'))
#
# def start_server(server_address):
#     my_server = server.ThreadingHTTPServer(server_address, Handler)
#     print(str(server_address) + ' Waiting for POST requests...')
#     my_server.serve_forever()
#
# def start_local_server_on_port(port):
#     p = Process(target=start_server, args=(('127.0.0.1', port),))
#     p.start()
#
# if(__name__ == '__main__'):
#     start_local_server_on_port(8011)
#     start_local_server_on_port(8012)
