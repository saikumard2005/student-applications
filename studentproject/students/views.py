from django.http import HttpResponse
from .models import Student

def student_list(request):
    students = Student.objects.all()

    html = "<h1>Student Information</h1>"
    html += "<table border='1' cellpadding='10'>"
    html += "<tr><th>ID</th><th>Name</th><th>Course</th><th>Marks</th></tr>"

    for student in students:
        html += (
            f"<tr><td>{student.id}</td>"
            f"<td>{student.name}</td>"
            f"<td>{student.course}</td>"
            f"<td>{student.marks}</td></tr>"
        )

    html += "</table>"
    return HttpResponse(html)