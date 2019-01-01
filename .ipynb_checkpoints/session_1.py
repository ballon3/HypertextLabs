# coding: utf-8
import pprint
from pypodio2 import api


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

"""
 c.__dir__ 
 
 returns...

['Application',
 'Area',
 'Connection',
 'Contact',
 'Conversation',
 'Embed',
 'Files',
 'Hook',
 'Item',
 'Notification',
 'Org',
 'Search',
 'Space',
 'Status',
 'Stream',
 'Task',
 'User',
 'View',
 '__builtins__',
 '__doc__',
 '__file__',
 '__name__',
 '__package__',
 'json',
 'urlencode']

"""


"""
 Workspace

(1) get info (url, url_label, space_id)
(2) get list of apps (app_id_lst)

"""
url_n = raw_input("workspace url_label:")
#org = raw_input("org:")
def wrkSpace():

    url = 'https://podio.com/applegate-solutions/' + url_n
    url2 = 'https://podio.com/hypertext-labs-co/' + url_n

    print(url2)

    space_id = c.Space.find_by_url(url2)

    print space_id


#wrkSpace()

"""
 Application(app_id_lst)

(1) iterate through each application 
(2) for e iter on app - get all_fields
(3) for e field get type and json struct

"""
apps = []
sid = raw_input("space id:")

def getApps(space_id):

    resp = c.Application.list_in_space(space_id)
    apps = []
    ids = []

    for i in resp:
        app_id = i['app_id']
        name = i['config']['name']
        
        apps.append(name)
        ids.append(app_id)
        print name 
        
    print apps
    return ids

#getApps(sid)

ap = raw_input("app id:")

def getFields(idx):

    #resp = c.Application.get_items(idx)
    #nx = json.loads(raw)

    esp = c.Application.find(idx)
    nx = esp['fields']
    types = []
    flabels = []
    fids = []
    
    for i in nx:
        label = i['label']
        typ = i['type']
        fid = i['field_id']
        flabels.append(label)
        types.append(typ)
        fids.append(fid)
        
    print flabels, types, fids

    """
    merge lists into json obj - sanitize label, lowercase etc..
    once merged each json item should populate two things 
    (1) django model definition 
    (2) 
    """
    


getFields(ap)




"""
for i in wrks_ndn:
    print i
    
"""
