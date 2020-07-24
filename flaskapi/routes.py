from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	try:
		language = langs[0]
	except IndexError:
		return jsonify([{'message':'Item Not found'},{'languages' : languages}]),404
	return jsonify({'language' : langs[0]}),200

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages}),200

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	try:
		langs[0]['name'] = request.json['name']
	except IndexError:
		return jsonify([{'message':'Item Not found'},{'languages' : languages}]),404
	return jsonify({'language' : langs[0]}),200

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [language for language in languages if language['name'] == name]
	try:
		languages.remove(lang[0])
	except IndexError:
		return jsonify([{'message':'Item Not found'},{'languages' : languages}]),404


	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=5002) #run app on port 5002 in debug mode