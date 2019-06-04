
# coding: utf-8

# In[1]:


import pprint
from pypodio2 import api
import json


# In[2]:



class networkInterface():
    
    """networkInterface authentication and network managment
    """
    
    client_id = "tester-2a2ebd"
    creds = {
        "organization": "applegate-solutions",
        "workspaceName": "ivxx-distro",
        "spaceId": "5809234",
        "clientId":"tester-2a2ebd",
        "clientSecret": "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG",
        "username": "ryan393brown@gmail.com",
        "password": "Cascadia3",    
    }
    
    credentials = None
    
    if credentials == None:
        
        clientId = creds["clientId"]
        clientSecret = creds["clientSecret"]
        username = creds["username"]
        password = creds["password"]
        organization = creds["organization"]
        workspaceName = creds["workspaceName"] 
        spaceId = creds["spaceId"]


    else:
 
        clientId = raw_input("Client ID:")
        clientSecret = raw_input("Client Secret:")
        username = raw_input("Username:")
        password = raw_input("Password:") 
        organization = raw_input("Organization Name:")
        workspaceName = raw_input("Workspace Name:")
        spaceId = raw_input("Workspace ID:")
        

    organizationUrl = "https://podio.com/" + organization
    workspaceUrl = organizationUrl + "/" + workspaceName
    
    print organizationUrl 
    print workspaceUrl 



    c = api.OAuthClient(
        clientId,
        clientSecret,
        username,
        password,    
    )
    
    


# In[3]:


x = networkInterface()
clientObj = x.c


# In[4]:


print clientObj


# In[5]:



def pullApp(appid):

    """pullFields retrieves fields for given application id

    Args:
        app (string): podio application id
    """

    cl = clientObj
    pp = pprint.PrettyPrinter(indent=2)

    resp = cl.Application.find(appid)
    
    resp['app_id']
    details = resp['config']
    appN = resp['url_label']
    pull = resp['url']
    push = resp['url_add']
    
    fields = resp['fields']

    #Create app dictionary to hold app Name,
    app = {
        "app": appN.encode('utf-8'),
        "appId": appid,
        "fields": []
    }

    #Append field to fields, in app dictionary 

    for field in fields:
        fapps = []
        label = field['label']
        typ = field['type']

        fid = field['field_id']

        if typ == 'calculation':

            rtyp = field['config']['settings']['return_type']

            app['fields'].append({"name": label.encode('utf-8'), "type": rtyp.encode('utf-8'), "id": fid})                                

        else:
            app['fields'].append({"name": label.encode('utf-8'), "type": typ.encode('utf-8'), "id": fid})

    return app 


# In[6]:


def author(data):
    with open('check.py', 'a') as f:

        #List of uniqe dicts based on the field type 
        fields = data['fields']
        
        app = data['app']

        django_model_class = "class {}(models.Model):\n".format(app.upper())
        f.write(django_model_class)

        for i in fields:

            fieldName = i['name']

            #Create Django Model Field Name 

            if i['type'] == 'text':
                dmField = "    {} = models.TextField(blank=True, null=True)\n".format(fieldName)



            elif i['type'] == 'date':
                dmField = "    {} = models.DateTimeField()\n".format(fieldName)


            elif i['type'] == 'relationship':
                dmField = "    {} = models.ForeignKey({})\n".format(fieldName, fieldName)

            elif i['type'] == 'member':
                dmField = "    {} = models.CharField(max_length=100)\n".format(fieldName)

            elif i['type'] == 'phone':
                dmField = "    {} = models.CharField(max_length=50)\n".format(fieldName)

            elif i['type'] == 'email':
                dmField = "    {} = models.EmailField()\n".format(fieldName)

            elif i['type'] == 'link':
                dmField = "    {} = models.URLField()\n".format(fieldName)

            elif i['type'] == 'number':
                dmField = "    {} = models.FloatField()\n".format(fieldName)

            elif i['type'] == 'organization':
                dmField = "    {} = models.URLField()\n".format(fieldName)

            elif i['type'] == 'image':
                dmField = "    {} = models.ImageField()\n".format(fieldName)

            elif i['type'] == 'money':
                dmField = "    {} = models.FloatField()\n".format(fieldName)

            elif i['type'] == 'progress':
                dmField = "    {} = models.IntegerField(max_length=100)\n".format(fieldName)

            elif i['type'] == 'duration':
                dmField = "    {} = models.DurationField()\n".format(fieldName)

            elif i['type'] == 'location':
                dmField = "    {} = models.URLField()\n".format(fieldName)

            elif i['type'] == 'phone':
                dmField = "    {} = models.CharField(max_length=254)\n".format(fieldName)

            #Category needs to introspectively determine Charf CHOICES from exisitng categorires
            elif i['type'] == 'category':
                dmField = "    {} = models.CharField(max_length=254)\n".format(fieldName)
                #settingsDict = i['settings']
                #print appDict


            elif i['type'] == 'calculation':
                dmField = "    {} = models.FileField()\n".format(fieldName)

            elif i['type'] == 'tag':
                dmField = "    {} = models.FileField()\n".format(fieldName)

            else:
                dmField = "    NA{} = models.FileField()\n".format(i['type'])

            f.write(dmField)          
        f.write('\n')
        


    with open('schema.py', 'a') as s:
        k = data['app']

        schema_type_def = "class {0}Type(DjangoObjectType):\n    class Meta:\n        model = {0}\n".format(k)
        s.write(schema_type_def)
        s.write('\n')
    return "Generated Podio Application Django Models"



# In[7]:


def podioAuthor(data):
    author(data)


# In[8]:


def singleMod(clientObj, mod):
    resp = clientObj.Application.find(mod)
    appId = resp['app_id']
    details = resp['config']
    appN = resp['url_label']
    pull = resp['url']
    push = resp['url_add']
    fields = resp['fields']
    
    appDic = pullApp(mod)
    dmMod = podioAuthor(appDic)
    #Append field to fields, in app dictionary 
 
    return "Podio to Django App Migration"       
    


# In[9]:


workspace


# In[54]:


def pullWorkspace(spaceId):
    """
    This is a raw workspace pull 
    (1) unique app pre processing
    (2) config: description, name, permissions create/edit
    (4) url_label
    
    """
    workspace = clientObj.Application.list_in_space(spaceId)
    return workspace


# In[56]:


def generator(networkInterface, workspace):
    x = pullWorkspace(workspace)
    j = json.dumps(x)
    loa_names = []
    loa = []
    for i in x:
        loa.append(i['app_id'])
        print i['url_label']
        
    
    for i in loa:
        singleMod(clientObj, i)
    return 


# In[ ]:


generator(clientObj, '5809234')


# In[ ]:


def commander():
    url_label = raw_input("URL Label:")
    generator(clientObj, '')

