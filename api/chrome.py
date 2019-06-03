# coding: utf-8
import pprint
from pypodio2 import api
import json

data = {}



client_id = "tester-2a2ebd"
client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
username = "ryan393brown@gmail.com"
password = "Cascadia3"

podioUrl = "https://podio.com/hypertext-labs-co/"
wrkSpaceUrl = "https://podio.com/hypertext-labs-co/"
wrkSpace = "body-back-company" 
sid = "5809234"


c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)

url_n = "ivxx-distro"

#org = raw_input("org:")
#wrkSpace()


apps = []
def wrkSpace(url_slug):

    url = 'https://podio.com/applegate-solutions/' + url_slug
    url2 = 'https://podio.com/hypertext-labs-co/' + url_slug

    print(url)

    space_id = c.Space.find_by_url(url)

    print space_id

wrkSpace(url_n)

def getApps(space_id):

    resp = c.Application.list_in_space(space_id)
    apps = []
    ids = []

    for i in resp:
        app_id = i['app_id']
        ids.append(app_id)
    return ids

d = getApps(sid)
print type(d)
#print d
def getFields(idx):

    #resp = c.Application.get_items(idx)
    #nx = json.loads(raw)
    #print idx
    for a in idx:
        #print a
                
        fids = []
        
        esp = c.Application.find(a)
        nx = esp['fields']
        appN = esp['url_label']
       # print nx

        
        for i in nx:
            fapps = []
            label = i['label']
            typ = i['type']
            
            fid = i['field_id']
            appFields = []
            if typ == 'calculation':
                rtyp = i['config']['settings']['return_type']
                #pl = (fid, label.encode('utf-8'), rtyp.encode('utf-8'))
                #fapps.append(tpl)
                fields = {
                            "name": label.encode('utf-8'),
                            "type": rtyp.encode('utf-8'),
                            "id": fid,
                        }
                
                return fields
                                
        
            else:
                #tpl = (fid, label.encode('utf-8'), typ.encode('utf-8'))
                #fapps.append(tpl)
                fields = {
                            "name": label.encode('utf-8'),
                            "type": typ.encode('utf-8'),
                            "id": fid,
                        }
                return fields
            
            appFields.append(fields)
            print appFields
            
            
            data['apps'] = []
            data['apps'].append({
                "app": appN,
                "appId": a,
                "fields": appFields
            })
        

 

    # Writing JSON data



#getFields(d)


class networkInterface():
    """networkInterface authentication and network managment
    """

    client_id = "tester-2a2ebd"

    if client_id:
        client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
        username = "ryan393brown@gmail.com"
        password = "Cascadia3"
    else:
        client_id = raw_input("Client ID:")
        client_secret = raw_input("Client Secret:")
        username = raw_input("Username:")
        password = raw_input("Password:")

    who = None 

    if who:
        workspaceName = "ivxx-distro" 
        spaceId = "5809234"
    
    organizationUrl = "https://podio.com/" + 
    workspaceUrl = "hhttps://podio.com/applegate-solutions/ivxx-distro"

    else:
        organizationUrl = raw_input("Organization URL:")
        workspaceUrl = raw_input("Workspace URL:")
        username = raw_input("Username:")
        password = raw_input("Password:")

    orgUrl = "https://podio.com/applegate-solutions/"
    workspaceUrl = "hhttps://podio.com/applegate-solutions/ivxx-distro"
    wrkSpace = "ivxx-distro" 
    spcId = "5809234"


    c = api.OAuthClient(
        client_id,
        client_secret,
        username,
        password,    
    )

networkInterface()

class podioInterface():

    def pullWorkspace():
        
        pass

        
    def pullApps(spaceId):
        
        resp = c.Application.list_in_space(spaceId)
        apps = []
        ids = []

        for i in resp:
            app_id = i['app_id']
            ids.append(app_id)

        return ids

        #d = getApps(sid)
        #resp = c.Application.get_items(idx)

        for app in apps:
                    
            fids = [] 
            resp = c.Application.find(a)
            fields = resp['fields']
            appName = resp['url_label']
            
            pass
        
        
    def pullFields(app):

        """pullFields retrieves fields for given application id
        
        Args:
            app (string): podio application id
        """
             
        fids = []
        
        resp = c.Application.find(app)
        fields = resp['fields']
        appN = resp['url_label']

        
        #Create app dictionary to hold app Name, app Id, and the apps template fields

        app = {
            "app": appN,
            "appId": a,
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
                
                app['fields'].append(
                    {
                        "name": label.encode('utf-8'),
                        "type": rtyp.encode('utf-8'),
                        "id": fid, 
                    }                    
                )
                                
        
            else:

                app['fields'].append(
                    {
                        "name": label.encode('utf-8'),
                        "type": typ.encode('utf-8'),
                        "id": fid,
                    }
                )
        
        print app





    def pushWorkspace():
        pass
    
    def pushApps():
        pass
    
    def pushFields():
        pass



class djInterface():

    def workspace2App():
        pass

    def app2Model():
        pass

    def fields2Model():
        pass

