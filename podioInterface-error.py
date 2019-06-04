
# coding: utf-8

# In[30]:


import pprint
from pypodio2 import api
import json


# In[31]:



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
    
    


# In[40]:


ApiInt = networkInterface().c


# In[43]:



def pullWorkspace(cl, spaceId):
    """
    This is a raw workspace pull 
    (1) unique app pre processing
    (2) config: description, name, permissions create/edit
    (4) url_label
    
    """
    workspace = cl.Application.list_in_space(spaceId)
    return workspace
#pullWorkspace(ApiInt, '5809234')


# In[35]:


cl = networkInterface().c
pp = pprint.PrettyPrinter(indent=2)

#resp = cl.Application.find('20157560')
#print resp['url_label']
#pullWorkspace("5809234")


# In[50]:


def wire(appDict):
    app = appDict['app']
    fields = appDict['fields']
    
    #Create Django Model Class Name 
    dmClass = "class {}(models.Model):\n".format(app.upper())
    print dmClass
    
    for i in fields:
        
        fieldName = i['name']
        
        #Create Django Model Field Name 

        if i['type'] == 'text':
            dmField = "    {} = models.TextField(blank=True, null=True)\n".format(fieldName)

            return dmField  
            
        elif i['type'] == 'date':
            dmField = "    {} = models.DateTimeField()\n".format(fieldName)
            return dmField  
            
        elif i['type'] == 'relationship':
            dmField = "    {} = models.ForeignKey({})\n".format(fieldName, fieldName)
            return dmField  
            
        elif i['type'] == 'member':
            dmField = "    {} = models.CharField(max_length=100)\n".format(fieldName)
            return dmField  
            
        elif i['type'] == 'phone':
            dmField = "    {} = models.CharField(max_length=50)\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'email':
            dmField = "    {} = models.EmailField()\n".format(fieldName)
            return dmField
                        
        elif i['type'] == 'link':
            dmField = "    {} = models.URLField()\n".format(fieldName)
            return dmField
                   
        elif i['type'] == 'number':
            dmField = "    {} = models.FloatField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'organization':
            dmField = "    {} = models.URLField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'image':
            dmField = "    {} = models.ImageField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'money':
            dmField = "    {} = models.FloatField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'progress':
            dmField = "    {} = models.IntegerField(max_length=100)\n".format(fieldName)
            return dmField
                    
        elif i['type'] == 'duration':
            dmField = "    {} = models.DurationField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'location':
            dmField = "    {} = models.URLField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'phone':
            dmField = "    {} = models.CharField(max_length=254)\n".format(fieldName)
            return dmField
            
        #Category needs to introspectively determine Charf CHOICES from exisitng categorires
        elif i['type'] == 'category':
            dmField = "    {} = models.CharField(max_length=254)\n".format(fieldName)
            #settingsDict = i['settings']
            #print appDict
            return i
            
        
        elif i['type'] == 'calculation':
            dmField = "    {} = models.FileField()\n".format(fieldName)
            return dmField
            
        elif i['type'] == 'tag':
            dmField = "    {} = models.FileField()\n".format(fieldName)
            return dmField
        
        else:
            return i['type']


# In[52]:


def pullFields(appid):

    """pullFields retrieves fields for given application id

    Args:
        app (string): podio application id
    """

    cl = networkInterface().c
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





# In[54]:


x = pullFields('20746674')


# In[55]:


wire(x)


# In[31]:


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


# In[32]:


x = loa("5809234")
for i in x:
    print i


# In[19]:


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



# In[20]:


def podioAuthor(data):
    for i in data:
        author(data)


# In[21]:


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


# In[25]:


def generator(workspace):
    listofApps = loa(workspace)
    
    for i in listofApps:
    
        print i
        app = pullFields(i)
        #print app
        podioAuthor(app)
        


# In[26]:


loa("5809234")


# In[27]:


generator("5809234")


# In[15]:


CHOICES = [

Text =TextField
Category*=CharField.choices 
Date == DateTimeField
Relationship = ForeignKeyField
Member* = CharField
Phone = CharField max 30
Email = EmailField
Link = URLField
Number = FloatField
Organization = URLField 
Image = ImageField
Money = FloatField 
Progress = IntegerField max 100
Duration = DurationField
Location = URLField 
Calculation = BinaryField (idk yet) 
]

