How to get and use access token from LinkedIn API
This code snippet shows how to get and use an access token from LinkedIn API to access your own profile information.

#Prerequisites

You need to create an app on LinkedIn Developer Platform and get the client ID and client secret. You can follow this guide: https://docs.microsoft.com/en-us/linkedin/shared/authentication/registration
You need to have a redirect URL that has been registered with your app. This URL will receive the authorization code after the user grants permission to your app.
You need to have a scope that defines what kind of data you want to access. For this example, we use w_member_social and r_liteprofile scopes. You can find more details about scopes here: https://docs.microsoft.com/en-us/linkedin/shared/authentication/authentication-scopes
You need to install requests library in Python to deal with REST APIs.
Steps
```Python
Import requests library.
import requests # To deal with REST APIs
Define the variables for the client ID, client secret, organization ID, base URL, redirect URL and scope.
# Get the ClientID and ClientSecret to get the access token
client_id       = "Get it from Linkedin after creating APP"
client_secret   = "Get it from Linkedin after creating APP"
organization_id = "Get it from URL of your org page"


base_url = "https://www.linkedin.com/oauth/v2/authorization"
redirect_uri = "Redirect URL which has been mentioned while creating app"
scope = "w_member_social,r_liteprofile"
Construct the authorization URL with the parameters.
url = f"{base_url}?response_type=code&client_id={client_id}&state=random&redirect_uri={redirect_uri}&scope={scope}"
```
Open the authorization URL in a browser and authorize your app. After that, you will be redirected to your redirect URL with an authorization code in the query string.

Copy the authorization code from the query string and assign it to a variable.

##Click the url and Authorize after that get auth_code from url

```Python
auth_code ="from url after authrizing the url"
Define the access token URL and payload with grant type, authorization code, redirect URI, client ID and client secret.
url_access_token = "https://www.linkedin.com/oauth/v2/accessToken"

payload = {
    'grant_type' : 'authorization_code',
    'code' : auth_code,
    'redirect_uri' : redirect_uri,
    'client_id' : client_id,
    'client_secret' : client_secret
}
```
Make a POST request to the access token URL with payload as parameters and get the response as JSON format.
```Python
response = requests.post(url=url_access_token, params=payload)
response_json = response.json()
print(response_json)
Extract the access token from the response JSON and assign it to a variable.
access_token = response_json['access_token']
Define your profile URL and header with authorization bearer token.
url = "https://api.linkedin.com/v2/me"

header = {
    'Authorization' : f'Bearer {access_token}'
}
```
Make a GET request to your profile URL with header as headers and verify as False (to avoid SSL certificate error).
```Python
response = requests.get(url=url, headers=header,verify=False)
print(response)
Get the response as JSON format and print it.
response_json_li_person = response.json()
print(response_json_li_person)
```
Extract your person ID from the response JSON and print it.
```Python
person_id = response_json_li_person['id']
print(person_id)  ##this is the id later to be used 
```
