# Experiment 9: Launch Web Application Using Google App Engine

## Aim

To use Google App Engine Launcher to launch a Python-based web application that displays student performance information through a web interface.

---

## Objectives

- To develop and configure a Python web application for Google App Engine.
- To model student performance details such as marks, average, grade, and pass/fail status using Object-Oriented Programming (OOP) in Python.
- To configure application routing and runtime environment using `app.yaml`.
- To launch and run the web application using Google App Engine Launcher.
- To access the web application on `http://localhost:8080/`.
- To inspect application request logs and understand basic application debugging.

---

## Introduction

Google App Engine is a Platform as a Service (PaaS) offered by Google Cloud. It allows developers to deploy and run web applications without directly managing the underlying servers.

In this experiment, a Python-based student performance application is created. The application uses an Object-Oriented Programming approach to store student details and calculate total marks, average marks, grade, and pass/fail status.

The application is configured using an `app.yaml` file and executed locally using Google App Engine development tools.

---

## Software & Platform Requirements

- **Cloud Platform:** Google App Engine
- **Development Tool:** Google App Engine Launcher
- **Programming Language:** Python
- **Web Browser:** Chrome / Firefox / Edge
- **Text Editor / IDE:** VS Code / Notepad++
- **Local Port:** `8080`

---

# Application Structure

```text
Experiment9_Google_App_Engine/
├── Readme.md
├── app.yaml
└── index.py
```

---

# File Contents

## 1. app.yaml

The `app.yaml` file contains the configuration information required by the Google App Engine environment.

```yaml
application: ae-01-trivial
version: 1
runtime: python
api_version: 1

handlers:
- url: /.*
  script: index.py
```

### Explanation

- `application`: Specifies the application identifier.
- `version`: Specifies the application version.
- `runtime`: Specifies the Python runtime environment.
- `api_version`: Specifies the App Engine API version.
- `handlers`: Defines URL routing rules for incoming requests.
- `url: /.*`: Matches all incoming URLs.
- `script: index.py`: Routes requests to the Python application.

---

## 2. index.py

The `index.py` file contains the application logic.

The application defines a `Student` class that stores student information and provides methods for calculating total marks, average marks, grade, and result status.

```python
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
```

---

# Procedure

## Step 1: Create the Application Directory

Create a project folder named:

```text
Experiment9_Google_App_Engine
```

Inside the folder, create the following files:

```text
Readme.md
app.yaml
index.py
```

---

## Step 2: Create the app.yaml File

Create a file named:

```text
app.yaml
```

Add the following configuration:

```yaml
application: ae-01-trivial
version: 1
runtime: python
api_version: 1

handlers:
- url: /.*
  script: index.py
```

Save the file.

The `app.yaml` file defines the application configuration and URL handling rules.

---

## Step 3: Create the index.py File

Create a Python file named:

```text
index.py
```

Add the Python application code provided above.

The program defines the `Student` class and the `ApplicationHandler` class.

---

## Step 4: Define the Student Class

The `Student` class stores the following information:

- Student name
- Roll number
- Marks

The constructor initializes these values:

```python
def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks
```

---

## Step 5: Calculate Total Marks

The `calculate_total()` method calculates the total marks:

```python
def calculate_total(self):
    return sum(self.marks)
```

For the given marks:

```text
85 + 92 + 78 + 88 + 90 = 433
```

Therefore:

```text
Total Marks = 433
```

---

## Step 6: Calculate Average Marks

The `calculate_average()` method calculates the average:

```python
def calculate_average(self):
    return self.calculate_total() / len(self.marks)
```

For the given marks:

```text
Average = 433 / 5
        = 86.60
```

Therefore:

```text
Average = 86.60
```

---

## Step 7: Calculate Grade

The `calculate_grade()` method assigns a grade based on the average marks.

The grading criteria are:

| Average | Grade |
|---:|:---|
| 90 and above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

Since the student's average is `86.60`, the grade is:

```text
A
```

---

## Step 8: Determine Pass/Fail Status

The `get_result()` method checks whether the student has scored at least 35 marks in every subject.

```python
def get_result(self):
    if all(mark >= 35 for mark in self.marks):
        return "PASS"
    return "FAIL"
```

Since all marks are greater than 35:

```text
Status = PASS
```

---

## Step 9: Create Student Object

The student information is initialized using:

```python
student = Student(
    "Amogha",
    "CS001",
    [85, 92, 78, 88, 90]
)
```

The application therefore contains:

```text
Name       : Amogha
Roll Number: CS001
Marks      : 85, 92, 78, 88, 90
```

---

## Step 10: Create HTTP Request Handler

The `ApplicationHandler` class handles HTTP GET requests:

```python
class ApplicationHandler(BaseHTTPRequestHandler):

    def do_GET(self):
```

When a user opens the application in a browser, the `do_GET()` method is executed.

It calculates:

```text
Total
Average
Grade
Result
```

and dynamically generates an HTML page.

---

## Step 11: Generate the HTML Response

The application creates an HTML document using Python formatted strings.

The generated page contains:

- Student name
- Roll number
- Subject marks
- Total marks
- Average
- Grade
- Pass/Fail status

The response is sent to the browser using:

```python
self.send_response(200)
self.send_header("Content-type", "text/html")
self.end_headers()

self.wfile.write(html.encode())
```

The HTTP status code `200` indicates that the request was successfully processed.

---

## Step 12: Start the Application Server

The application starts an HTTP server on port `8080`:

```python
server = HTTPServer(("localhost", 8080), ApplicationHandler)
```

The server displays:

```text
Server running at http://localhost:8080
```

The application continues running using:

```python
server.serve_forever()
```

---

## Step 13: Add Application to Google App Engine Launcher

1. Open **Google App Engine Launcher**.
2. Select:

```text
File → Add Existing Application
```

3. Browse to the `Experiment9_Google_App_Engine` directory.
4. Select the directory containing:

```text
app.yaml
index.py
```

5. Add the application to the launcher.

---

## Step 14: Run the Application

1. Select the application from the Google App Engine Launcher.
2. Click the **Run** button.
3. Wait for the application to start.
4. Verify that the application is running on port `8080`.

The application should be available at:

```text
http://localhost:8080/
```

---

## Step 15: Open the Application in a Web Browser

Open a web browser and enter:

```text
http://localhost:8080/
```

The Student Performance Report should be displayed.

---

# Expected Output

```text
Student Performance Report

Name: Amogha

Roll Number: CS001

Marks

Cloud Computing: 85
Computer Networks: 92
Database Systems: 78
Operating Systems: 88
Machine Learning: 90

Result

Total Marks: 433
Average: 86.60
Grade: A
Status: PASS
```

---

# Step 16: Modify Student Details

The application can be tested with different student information.

For example:

```python
student = Student(
    "Amogha",
    "CS002",
    [75, 82, 69, 91, 85]
)
```

Save the changes and refresh:

```text
http://localhost:8080/
```

The application will display the updated student performance information.

---

# Step 17: View Application Logs

Application logs can be used to monitor requests and identify errors.

Refresh the application in the browser and observe the corresponding HTTP request.

A successful request may appear similar to:

```text
GET / HTTP/1.1 200
```

The `200` status indicates that the request was successfully processed.

Logs are useful for debugging application configuration and execution problems.

---

# Application Workflow

The overall workflow of the application is:

```text
User opens browser
        ↓
http://localhost:8080/
        ↓
HTTP GET request
        ↓
ApplicationHandler.do_GET()
        ↓
Student object
        ↓
Calculate Total
        ↓
Calculate Average
        ↓
Calculate Grade
        ↓
Calculate PASS/FAIL
        ↓
Generate HTML
        ↓
Send HTTP Response
        ↓
Student Performance Report displayed
```

---

# Key Concepts Demonstrated

## 1. Cloud Application Hosting

Google App Engine provides a platform for running web applications without directly managing physical servers.

## 2. Object-Oriented Programming

The application uses a `Student` class to encapsulate student information and related operations.

## 3. HTTP Request Handling

`BaseHTTPRequestHandler` is used to process HTTP GET requests.

## 4. Dynamic HTML Generation

The HTML content is generated dynamically using Python data.

## 5. Application Configuration

The `app.yaml` file defines the application's runtime and request routing configuration.

## 6. Application Logging

HTTP request logs can be inspected to monitor application behavior and debug errors.

---

# Result

The Python-based student performance web application was successfully created using Object-Oriented Programming concepts.

The application was configured using `app.yaml` and implemented using `index.py`. It was launched locally and accessed through:

```text
http://localhost:8080/
```

The application successfully displayed the student's name, roll number, subject marks, total marks, average, grade, and pass/fail status.

---

# Conclusion

This experiment demonstrated the basic process of configuring and running a Python web application using Google App Engine development tools.

The experiment provided practical knowledge of App Engine configuration, Python HTTP request handling, Object-Oriented Programming, dynamic HTML generation, application execution, and request logging.

The student performance application successfully calculated and displayed the required academic information through a web interface.