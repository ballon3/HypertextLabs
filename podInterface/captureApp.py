

def pullWorkspace(cl, spaceId):
    """
    This is a raw workspace pull 
    (1) unique app pre processing
    (2) config: description, name, permissions create/edit
    (4) url_label
    
    """
    workspace = cl.Application.list_in_space(spaceId)
    return workspace

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

            print  dmField  
            
        elif i['type'] == 'date':
            dmField = "    {} = models.DateTimeField()\n".format(fieldName)
            print  dmField  
            
        elif i['type'] == 'relationship':
            dmField = "    {} = models.ForeignKey({})\n".format(fieldName, fieldName)
            print  dmField  
            
        elif i['type'] == 'member':
            dmField = "    {} = models.CharField(max_length=100)\n".format(fieldName)
            print  dmField  
            
        elif i['type'] == 'phone':
            dmField = "    {} = models.CharField(max_length=50)\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'email':
            dmField = "    {} = models.EmailField()\n".format(fieldName)
            print  dmField
                        
        elif i['type'] == 'link':
            dmField = "    {} = models.URLField()\n".format(fieldName)
            print  dmField
                   
        elif i['type'] == 'number':
            dmField = "    {} = models.FloatField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'organization':
            dmField = "    {} = models.URLField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'image':
            dmField = "    {} = models.ImageField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'money':
            dmField = "    {} = models.FloatField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'progress':
            dmField = "    {} = models.IntegerField(max_length=100)\n".format(fieldName)
            print  dmField
                    
        elif i['type'] == 'duration':
            dmField = "    {} = models.DurationField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'location':
            dmField = "    {} = models.URLField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'phone':
            dmField = "    {} = models.CharField(max_length=254)\n".format(fieldName)
            print  dmField
            
        #Category needs to introspectively determine Charf CHOICES from exisitng categorires
        elif i['type'] == 'category':
            dmField = "    {} = models.CharField(max_length=254)\n".format(fieldName)
            #settingsDict = i['settings']
            #print appDict
            print  i
            
        
        elif i['type'] == 'calculation':
            dmField = "    {} = models.FileField()\n".format(fieldName)
            print  dmField
            
        elif i['type'] == 'tag':
            dmField = "    {} = models.FileField()\n".format(fieldName)
            print  dmField
        
        else:
            print  i['type']