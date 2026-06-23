from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Fake database in memory
students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Get list of all students
    ---
    responses:
      200:
        description: A list of students
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    return jsonify(students)

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Get a specific student by ID
    ---
    parameters:
      - name: student_id
        in: path
        type: integer
        required: true
        description: The ID of the student
    responses:
      200:
        description: Student details
      404:
        description: Student not found
    """
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

@app.route('/api/students', methods=['POST'])
def add_student():
    """
    Add a new student
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Student
          required:
            - id
            - name
          properties:
            id:
              type: integer
            name:
              type: string
    responses:
      201:
        description: Student added successfully
    """
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)
