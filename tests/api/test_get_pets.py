import pytest


class TestPetsAPI:
    def test_get_pet_by_id(self, api_client):
        response = api_client.get("/pet/1")
        assert response.status_code == 200
        payload = response.json()
        assert payload["id"] == 1
        assert payload["name"] == "doggie"
 
#http://rahulshettyacademy.com
#'visit-month'
cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com',allow_redirects=False,cookies=cookie,timeout=1)
#301,200
#print(response.history)
print(response.status_code)
 
 
se = requests.session()
se.cookies.update({'visit-month':'February'})
 
res = se.get("https://httpbin.org/cookies",cookies={'visit-year':'2022'})
print(res.text)
 
#Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
r= requests.post(url,files=files)
print(r.status_code)
print(r.text)