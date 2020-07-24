from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

data = [{'employee_id': i+1} for i in range(1000)]

def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj

class Employees(Resource):
    def get(self):
        return jsonify(get_paginated_list(
        data, 
        '/employees', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    ))

    def post(self):
        return jsonify({'message':'this is a post request'})
    

class Employees_one(Resource):
    def get(self, employee_id):
        return jsonify({'employee_id':employee_id})
    
    def put(self,employee_id):
        return {'status':'Employee updated successfully'}

    def delete(self,employee_id):
        return {'status':'Employee Deleted successfully'}

api.add_resource(Employees, '/employees')
api.add_resource(Employees_one, '/employees/<employee_id>') 

if __name__ == '__main__':
    app.run(port='5002', debug=True)