# coding: utf-8

from pypodio2 import api
c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)
client_id = "tester-2a2ebd"
client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
username = "ryan393brown@gmail.com"
password = "Cascadia3"

podioUrl = "https://podio.com/hypertext-labs-co/"
wrkSpaceUrl = "https://podio.com/hypertext-labs-co/"
wrkSpace = "body-back-company"
c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)
c.Areas.objects.all()
c.__dict__()
c.__dir__()
c.Area.__init__()
c.Area.sanitize_id(20984103)
c.Area(20984103)
c.Area()
c.Area.get_options()
c.Item.fin(171818192)
c.Item.find(171818192)
c.Item.find(180601912)
c.Item.find(http:\/\/api.podio.com\/item\/180601912)
c.Item.find(180601912)
c.Item.find('180601912')
c.Item.find(21896052)
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
c.Application.list_in_space(6319170)
pprint.pprint(c.Application.list_in_space(6319170))
import pprint
pprint.pprint(c.Application.list_in_space(6319170))
pprint.pprint(c.Application.list_in_space(6319170)[app_id])
resp = c.Application.list_in_space(6319170)
type(resp)
for i in resp
for i in resp:
    print i[app_id]
    
for i in resp:
    print i
    
    
for i in resp:
    pprint.pprint(i)
    
    
    
import ast
ast.literal_eval(resp)
import json
print resp
json_acceptable_string = resp.replace("'", "\"")
json.dumps(resp)
new = json.dumps(resp)
pprint.pprint(new)
resp[app_id}
resp[app_id]
data = json.loads(new)
data
pprint.pprint(data)
resp['app_id']
resp[0]


    
for i in resp:
    app_id = i['app_id']
    name = i['config']['name']
    print name 
    print app_id
    
get_ipython().magic(u'save session_2 0-52')
