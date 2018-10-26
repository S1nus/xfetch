from requests_futures.sessions import FuturesSession
import base64
import json
import OrionTypes

class Orion:
    session = FuturesSession()
    
    authenticated = False
    token = None

    apiRequests = []
    
    def authenticate(self, username, password):
        encodedauth = base64.b64encode(bytes(username+":"+password, "utf-8"))
        headers = {'Authorization' : "Basic " + str(encodedauth, "utf-8")}
        authReq = self.session.get('https://api.orionadvisor.com/api/v1/security/token', headers=headers)        
        authResponse = authReq.result()
        if (not authResponse.status_code == 200):
            raise PermissionError("Invalid Orion credentials")
        elif (authResponse.status_code == 200):
            jsonResponse = str(authResponse.content, "utf-8")
            objResult = json.loads(jsonResponse)
            self.token = objResult['access_token']
            self.authenticated = True
        else:
            raise PermissionError("Error sending authentication request")

    def fpFocusRequest(self, name, date):
        print("Starting request...")
        if (self.authenticated):
            p = OrionTypes.generatePayLoad_13095(name, date)
            headers = {'Authorization' : "Session " + self.token, "Content-Type" : "application/json"}
            req = self.session.post("https://api.orionadvisor.com/api/v1/reporting/custom/13095/generate/table", headers=headers, data=p)
            resp = req.result()
            print("received response.")
            print(resp.content)
        else:
            raise PermissionError("You are not authenticated with Orion!")
        
        
orion = Orion()
