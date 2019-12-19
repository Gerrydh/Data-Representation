from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

acts=[
    {"id": 1,"Name":"Joe", "totalVotes":4},
    {"id": 2,"Name":"REM", "totalVotes":5},
    ]

nextID=3
#@app.route('/')
#def index():
 #   return "Hello, World!"
 #"http://127.0.0.1:5000/books"
@app.route('/acts')
def getAll():
     return jsonify(acts)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/acts/<int:id>')
def findByID(id):
    foundActs = list(filter(lambda t: t['id']== id, acts))
    if len(foundActs)== 0:
        return jsonify({}), 204

    return jsonify(foundActs[0])

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"Coding\",\"Author\":\"Dummies\",\"Price\":56}" http://127.0.0.1:5000/books
@app.route('/acts', methods=['POST', 'GET'])
def create():
    global nextID
    if not request.json:
        abort(400)
        #other checking
    act = {
        "id": nextID,
        "Name": request.json['Name'],
        "totalVotes":0
        }
    nextID += 1
    acts.append(act)
    return jsonify(act)

@app.route('/acts/<int:id>', methods=['DELETE'])
def delete(id):
    foundActs = list(filter(lambda t: t['id']== id, acts))
    if (len(foundActs) == 0):
        abort(404)
    acts.remove(foundActs[0])
    return jsonify({"done":True})

@app.route('/votes/<int:actId>', methods=['POST', 'GET'])
def addVote(actId):
    foundActs=list(filter(lambda t: t['id']== actId, acts))
    if len(foundActs)==0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'votes' in request.json or type(request.json['votes']) is not int:
        abort(401)
    newVotes = request.json['votes']

    foundActs[0]['totalVotes'] += newVotes

    return jsonify(foundActs[0])

@app.route('/votes/leaderboard')
def getleaderboard():
    acts.sort(key=lambda x: x['totalVotes'], reverse=True)
    return jsonify(acts)

if __name__=='__main__':
    app.run(debug=True)