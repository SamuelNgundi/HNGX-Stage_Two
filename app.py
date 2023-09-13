from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow

### Create an instance of flask
app = Flask(__name__)


db = SQLAlchemy()
ma = Marshmallow()

mysql = MySQL(app)


#Create a model for our table

class Person(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(130), nullable=False)
    age= db.Column(db.Integer, nullable=False)
    email= db.Column(db.String(130), unique=True, nullable=False)


    def __init__(self, name, age, email) :
        self.name=name
        self.age=age
        self.email=email
    
class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'age', 'email')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

##MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://samuelwngundi:python2023@samuelwngundi.mysql.pythonanywhere-services.com/samuelwngundi$person'

##SQLITE
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
db.init_app(app)
with app.app_context():
    db.create_all()

# Configure method for pOST to Create a person

@app.route('/api', methods=['POST'])
def add_person():
    _json = request.json
    name = _json['name']
    if not isinstance(name, str):
            return jsonify({"Error": "Name must be a string"}), 400
    existing_person = Person.query.filter_by(name=name).first()
    if existing_person:
            return jsonify({"Error": "Name is already registered"}), 400
    age = _json['age']
    email = _json['email']
    new_person = Person(name=name, age=age, email=email)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"Message": "Created new person"}), 201


# Configure method for GET

@app.route('/api', methods=['GET'])
def get_person():
    persons = []
    data = Person.query.all()
    persons = persons_schema.dump(data)
    return jsonify(persons)

# Configure method for GET to get a person by their id

@app.route('/api/<int:user_id>', methods=['GET'])
def person_byid(user_id):
    person = Person.query.get(user_id)
    data = person_schema.dump(person)
    return jsonify(data)

# Configure method for PUT to edit details of a person by their ID

@app.route('/api/<int:user_id>', methods=['PUT'])
def edit_person(user_id):
    person = Person.query.get(user_id)
    if person is None:
        return jsonify ({"Error": "this person doesn't exist"}), 404
    _json = request.json
    person.name = _json['name']
    new_name = _json['name']
    if not isinstance(new_name, str):
            return jsonify({"Error": "Name must be a string"}), 400
    person.age =_json['age']
    person.email= _json['email']
    db.session.commit()
    return jsonify({"Message": "this person has been edited"})

# Configure method for DELETE to delete details of a person by their ID

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)
    if person is None:
        return jsonify(f"Error: this person doesn't exist"), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({"Message": "this person has been deleted"})


if __name__ == "__main__":
    app.run(debug=True)