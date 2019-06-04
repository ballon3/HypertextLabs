
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
    
    