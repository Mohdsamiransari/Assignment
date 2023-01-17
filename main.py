import json
from jinja2 import Environment,FileSystemLoader

#opening/loading the project.json file
with open("project.json","r") as d:
    project = json.load(d)


#connecting the template folder and getting the index.html file to work with the json file
fileloader = FileSystemLoader("templates")
env = Environment(loader=fileloader)


rendered = env.get_template("index.html").render(project = project)


#write a new index.html file in site folder to get the result
filename = "index.html"
with open(f"./site/{filename}", "w") as f:
    #rending the template index.html into site index.html
    f.write(rendered)