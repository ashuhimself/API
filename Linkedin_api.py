import requests                 # To deal with REST APIs

# Get the ClientID and ClientSecret to get the access token
client_id       = "Get it from Linkedin after creating APP"
client_secret   = "Get it from Linkedin after creating APP"
organization_id = "Get it from URL of your org page"


base_url = "https://www.linkedin.com/oauth/v2/authorization"
redirect_uri = "Redirect URL which has been mentioned while creating app"
scope = "w_member_social,r_liteprofile"


url = f"{base_url}?response_type=code&client_id={client_id}&state=random&redirect_uri={redirect_uri}&scope={scope}"

##Click the url and Authorize after that get auth_code from url

auth_code ="from url after authrizing the url"

url_access_token = "https://www.linkedin.com/oauth/v2/accessToken"


payload = {
    'grant_type' : 'authorization_code',
    'code' : auth_code,
    'redirect_uri' : redirect_uri,
    'client_id' : client_id,
    'client_secret' : client_secret
}

response = requests.post(url=url_access_token, params=payload)
response_json = response.json()
print(response_json)



access_token = "AQWeOOvnlrHCOo38zN2jxVZp31s4RY7Ab_tPvWJj3pMypjgyeD_lZ2edDH50tUYYBmNeqcBfOwN3SmU66yRas8IpJBR-_S4fMqRL9UtfWoBT8K-ccu4TA4jyC79Dsp4MwtAN4G8kS5xI4aQKqnZ1vvnAs_CnYAYGPC1FNjAhiyUcb_HojGpcXaISY-XXLIgrllxCsf1k7VX28YfwWXgml5fYQ2IW1C7ZPme_JmP0UwGbX_HBpZN_fJUhvPRHVUo3i1Sw0Hm9i9GIhpSWElrpcUavAcFzhJMgJGcFaeN5-L98wFnVuy1BStuoBrKPO-IIysTbLd_BAwETo8_WMjuXtcA9zuchaQ"


url = "https://api.linkedin.com/v2/me"

header = {
    'Authorization' : f'Bearer {access_token}'
}

response = requests.get(url=url, headers=header,verify=False)
print(response)
response_json_li_person = response.json()
print(response_json_li_person)

person_id = response_json_li_person['id']
print(person_id)  ##this is the id later to be used 