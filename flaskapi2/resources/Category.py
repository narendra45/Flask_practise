from flask import request
from flask_restful import Resource
from Model import db, Category, CategorySchema

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        try:
            categories = categories_schema.dump(categories)
        except:
            return {'error':'Data is empty'},400
        return {'status': 'success', 'data': categories}, 200
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data),None
        if errors:
            return errors, 422
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(
            name=json_data['name']
            )

        db.session.add(category)
        db.session.commit()
        result = category_schema.dump(category)

        return { "status": 'success', 'data': result }, 201
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).first()
        if not category:
            return {'message': 'Category does not exist'}, 400
        category.name = data['name']
        db.session.commit()

        result = category_schema.dump(category)

        return { "status": 'success', 'data': result }, 204
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = category_schema.load(json_data),None
        if errors:
            return errors, 422

        category = Category.query.filter_by(id=int(data['id'])).first()
        if not category:
            return {'message': 'Category does not exist'}, 204
        result = category_schema.dump(category)
        db.session.delete(category)
        db.session.commit()
        print(result)

        return { "status": 'success', 'data': result}, 204
