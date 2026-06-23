from flask import Flask, jsonify, request

app = Flask(__name__)

# دیتابیس فرضی در حافظه (همان آرایه‌ای که استاد خواسته)
students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"}
]

# ۱. دریافت لیست همه دانشجویان
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

# ۲. دریافت اطلاعات یک دانشجوی خاص با شناسه
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# ۳. اضافه کردن دانشجوی جدید
@app.route('/api/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)
