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

sid = "5809234"
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


def getFields(idx):

    #resp = c.Application.get_items(idx)
    #nx = json.loads(raw)
    #print idx
    apps = []
    for a in idx:
        #print a
                
        types = []
        flabels = []
        fids = []
        
        esp = c.Application.find(a)
        nx = esp['fields']
        appN = esp['url_label']
       # print nx
        data = []
        data.append({
            "app": appN,
            "appId": a,
            "fields": []
        })
        
        for i in nx:
            fapps = []
            label = i['label']
            typ = i['type']
            
            fid = i['field_id']

            if typ == 'calculation':
                rtyp = i['config']['settings']['return_type']
                #pl = (fid, label.encode('utf-8'), rtyp.encode('utf-8'))
                #fapps.append(tpl)
                data['apps']['fields'].append({
                    {
                        "name": label.encode('utf-8'),
                        "type": rtyp.encode('utf-8'),
                        "id": fid, 
                    }                    
                })
                                
        
            else:
                #tpl = (fid, label.encode('utf-8'), typ.encode('utf-8'))
                #fapps.append(tpl)
                data['apps']['fields'].append({
                    {
                        "name": label.encode('utf-8'),
                        "type": typ.encode('utf-8'),
                        "id": fid,
                    }
                })
    print data




getFields(d)





