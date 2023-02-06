import pymongo
import webbrowser
from jinja2 import Template

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["myDB"]
mycol = mydb["builds"]

student = []

tbl = "<tr><td>Build ID</td><td>Time Received</td><td>Status</td></tr>"
student.append(tbl)

for y in mycol.find():
    a = "<tr><td>%s</td>"%y['id']
    student.append(a)
    b = "<td>%s</td>"%y['time']
    student.append(b)
    c = "<td>%s</td></tr>"%y['status']
    student.append(c)


contents = '<table CLASS="table"> \
%s \
</table> \
</body> \
</html>' %(student)

filename = 'history.html'

def main(contents, filename):
    output = open(filename,"w")
    vals = {'replace': 'contents'}
    output.write(vals)
    output.close()

main(contents, filename)    
webbrowser.open(filename)