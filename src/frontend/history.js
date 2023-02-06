import pymongo
import webbrowser

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["myDB"]
mycol = mydb["person"]

student = []

tbl = "<tr><td>Name</td><td>Age</td><td>gender</td></tr>"
student.append(tbl)

for y in mycol.find():
    a = "<tr><td>%s</td>"%y['name']
    student.append(a)
    b = "<td>%s</td>"%y['age']
    student.append(b)
    c = "<td>%s</td></tr>"%y['gender']
    student.append(c)

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(student)

filename = 'info.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)