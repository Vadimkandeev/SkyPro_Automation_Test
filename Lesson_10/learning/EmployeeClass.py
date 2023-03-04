import requests


class EmployeeClass:

    def __init__(self, url):
        self.url = url 
    

    def get_token(self, user =  'bloom', password = 'fire-fairy'):  
        creds = {
        'username': user,
        'password': password
        }
        resp = requests.post("https://x-clients-be.onrender.com/auth/login", json=creds)
        return resp.json()["userToken"]
        
    
    #  Any GET request
    def employee_get(self, path, id):  

       status = requests.get(self.url+path+ str(id)).status_code
       body =  requests.get(self.url+path+ str(id)).json()
       return [body, status]
    #-------------------------------------------------------------
       


    # создание новой записи работника
    def employee_post(self, companyId, firstName, lastName, middleName, phone, url):
        new_employee = {        
        "companyId": companyId,
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "phone": phone,
        "url": url
        }
        my_headers={}
        my_headers["x-client-token"] = self.get_token() 
        resp = requests.post(self.url, headers=my_headers, json=new_employee)  
        #self.id_employee = resp.json()["id"]
        return [resp.json(), resp.status_code]
    #-------------------------------------------------------------
    


    # редактирование записи работника
    def employee_patch(self, employee_id, lastName, email, url, isActive):
        redact_worker = {
         "lastName": lastName,
         "email": email,
         "url": url,
         "isActive": isActive
        }
        my_headers={}
        my_headers["x-client-token"] = self.get_token() 
        resp = requests.patch(self.url + "/"+str(employee_id), json=redact_worker, headers=my_headers)
        resp_json = resp.json()
        resp_status = resp.status_code
        return [resp_json, resp_status] 
    #-------------------------------------------------------------
    
    

