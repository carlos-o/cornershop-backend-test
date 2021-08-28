# Documentation of services module Accounts
### Table of contents
* **[Signin](#Signin)**<br>
* **[Signout](#Signout)**<br>

## Signin
Grants access to a user to start in API

* Url

  http://127.0.0.1:8000/accounts/signin/

* Method

  **POST**

* Url Params

  **None**

* Data Params

    ```json
     {
        "username":"example",
        "password":"example123"
     } 
    ```

* Success Response:
   * code: 200
    ```json
    {
        "success": true,
        "code": 200,
        "data": {
            "id": 1,
            "last_login": "2021-08-20 22:09:15",
            "username": "admin",
            "first_name": "admin",
            "last_name": "admin",
            "email": "admin@admin.com",
            "is_active": true,
            "token": "e239f83efacc5ffb84fb622abffc2806eac46e8a"
        },
        "message": "ok"
    }
   ```  
* Error Response:
   
   In case username or password incorrect 
  * code: 400
   ```json
   {
    "success": false,
    "code": 400,
    "data": {},
    "message": "ValueError",
    "errors": "The username or password is incorrect"
   }
   ``` 
  or
  
  * case 401
  ```json
  {
    "success": false,
    "code": 401,
    "data": {},
    "message": "Permission Denied",
    "errors": "Account blocked, contact the administrators."
  }
  ```
  
  or
  
  * case: 500
   ```json
   {
        "detail": {
            "success": false,
            "code": 500,
            "data": {},
            "message": "Internal Server Error",
            "errors": {
                "error": [
                    "errors"
                ]
            }
        }
   }
  ```
  
* Notes:
 
  **None**
  
## Logout
**TOKEN IS REQUIRED**

add a header 
 
**Authorization**  token 74dafd9462f6c8df986723fccee1c08c2e564cd6


logout from server

* Url

  http://127.0.0.1:8000/accounts/signout/

* Method

  **POST**

* Url Params

  **None**

* Data Params

  **None**

* Success Response:
   * code: 200
   ```json
   {
    "detail": {
        "success": true,
        "code": 200,
        "data": {},
        "message": "ok"
    }
   }
   ```  
* Error Response:
  * case: 401
  ```json
  {
    "success": false,
    "code": 401,
    "data": {},
    "message": "Permission Denied",
    "errors": "Invalid Token"
  }
  ```
  
  or
  
  * case: 500
   ```json
   {
        "detail": {
            "success": false,
            "code": 500,
            "data": {},
            "message": "Internal Server Error",
            "errors": {
                "error": [
                    "errors"
                ]
            }
        }
   }
  ```
  
* Notes:
 
  **None**