
client_id = "tester-2a2ebd"
client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
username = "ryan393brown@gmail.com"
password = "Cascadia3"

podioUrl = "https://podio.com/hypertext-labs-co/"
wrkSpaceUrl = "https://podio.com/hypertext-labs-co/"
wrkSpace = "body-back-company" 

from pypodio2 import api
import requests 

c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)

class Podio(object):

    def getWorkspaces():
        """Get workspaces, id's
        """
    def getApps(auth, wrkUrl):
        """Get all apps in a podio workspace,   
        quit()
        Args:
            tkn (int): token for app auth
            wrkUrl (int): Workspace ID for api reference 
        """
    def getAppTemplate(app_id):
        """ Get Field Structure to auto generate GQL schema 
        """
    def genAppSchema()
    """ Generate a Graphql schema from the returned Json podio template + fields
    """
