from http.server import BaseHTTPRequestHandler, HTTPServer


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def get_result(self):
        if all(mark >= 35 for mark in self.marks):
            return "PASS"
        return "FAIL"


student = Student(
    "Amogha",
    "CS001",
    [85, 92, 78, 88, 90]
)


class ApplicationHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        total = student.calculate_total()
        average = student.calculate_average()
        grade = student.calculate_grade()
        result = student.get_result()

        html = f"""
        <html>
        <head>
            <title>Student Performance</title>
        </head>

        <body>
            <h1>Student Performance Report</h1>

            <p><b>Name:</b> {student.name}</p>
            <p><b>Roll Number:</b> {student.roll_no}</p>

            <h2>Marks</h2>

            <ul>
                <li>Cloud Computing: {student.marks[0]}</li>
                <li>Computer Networks: {student.marks[1]}</li>
                <li>Database Systems: {student.marks[2]}</li>
                <li>Operating Systems: {student.marks[3]}</li>
                <li>Machine Learning: {student.marks[4]}</li>
            </ul>

            <h2>Result</h2>

            <p><b>Total Marks:</b> {total}</p>
            <p><b>Average:</b> {average:.2f}</p>
            <p><b>Grade:</b> {grade}</p>
            <p><b>Status:</b> {result}</p>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode())


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), ApplicationHandler)

    print("Server running at http://localhost:8080")

    server.serve_forever()