import pprint
from pypodio2 import api
import json

from podInterface.networkInterface import * as ni
from podInterface.captureApp import * as capture


ApiInt = ni.networkInterface().c


def loa(workspace):
    print type(pullWorkspace(workspace))
    x = pullWorkspace(workspace)
    j = json.dumps(x)
    loa_names = []
    loa = []
    for i in x:
        loa.append(i['app_id'])
        print i['url_label']
    return loa

loa("5809234")

def generator(workspace):
    listofApps = loa(workspace)
    
    for i in listofApps:
    
        print i
        app = pullFields(i)
        #print app
        podioAuthor(app)
      

def author(data):
    with open('check.py', 'a') as f:

        fields = data['fields']
        app = data['app']

        django_model_class = "class {}(models.Model):\n".format(app.upper())
        print(f.write(django_model_class))

        for i in fields:
            n = i['name']

            django_model_field = "    {} = models.TextField(max_length=100)\n".format(n)
            f.write(django_model_field)          
            print(django_model_field)
        f.write('\n')


    with open('schema.py', 'a') as s:
        k = data['app']

        schema_type_def = "class {0}Type(DjangoObjectType):\n    class Meta:\n        model = {0}\n".format(k)
        s.write(schema_type_def)
        s.write('\n')
    return "Generated Podio Application Django Models"

