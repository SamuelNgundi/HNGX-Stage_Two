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
    name= db.Column(db.String(15), nullable=False)
    age= db.Column(db.Integer, nullable=False)
    email= db.Column(db.String(15), nullable=False)


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/person'

##SQLITE
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/api', methods=['POST'])
def add_person():
    _json = request.json
    name = _json['name']
    age = _json['age']
    email = _json['email']
    new_person = Person(name=name, age=age, email=email)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"Message": "Created new person"})



@app.route('/api', methods=['GET'])
def get_person():
    persons = []
    data = Person.query.all()
    persons = persons_schema.dump(data)
    return jsonify(persons)


@app.route('/api/user_id/<id>', methods=['GET'])
def person_byid(id):
    person = Person.query.get(id)
    data = person_schema.dump(person)
    return jsonify(data)

@app.route('/api/user_id/<id>', methods=['POST'])
def delete_person(id):
    person = Person.query.get(id)
    if person is None:
        return jsonify(f"Error: this person doesn't exist")
    db.session.delete(person)
    db.session.commit()
    return jsonify({"Message": "this person has been deleted"})

@app.route('/api/user_id/<id>', methods=['POST'])
def edit_person(id):
    person = Person.query.get(id)
    if person is None:
        return jsonify ({"Error": "this prodcut doesn't exist"})
    _json = request.json
    person.name = _json['name']
    person.age =_json['age']
    person.email= _json['email']
    db.session.commit()
    return jsonify({"Message": "this person has been edited"})

if __name__ == "__main__":
    app.run(debug=True)