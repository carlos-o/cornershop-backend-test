# Documentation of Services Module Order
### Table of contents
* **[Order](#Order)**<br>


## Order
### List Order
**TOKEN IS REQUIRED**

get the list of all order

* Url

  http://127.0.0.1:8000/order/

* Method

  **GET**

* Url Params

  **None**

* Data Params

  **None**

* Success Response:
   * code: 200
   ```json
    {
        "count": 1,
        "countItemsOnPage": "20",
        "current": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "menu": "menu del dia lunes",
                "rut": "23125620-2",
                "name": "carlos olivero",
                "option": "ensalada cesar",
                "customization": "con mucha salsa",
                "created_at": "2021-08-25 22:36:05"
            }
        ]
   }
   ```  
* Error Response:

  * case 401
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
  
  * code: 403
   ```json
   {
      "detail": "The access method is not allowed"
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
 
  **only admin user has permission to call this method**
  
### Create Order
**TOKEN IS REQUIRED**

Place an order from the menu

* Url

  http://127.0.0.1:8000/order/

* Method

  **POST**

* Url Params

  **None**

* Data Params

    ```json
     {
        "optionId": 1,
        "customization": "con mucha salsa"
     }
    ```

* Success Response:
   * code: 201
    ```json
   {
        "success": true,
        "code": 201,
        "data": {
            "id": 1,
            "menu": "menu del dia lunes",
            "rut": "23125620-2",
            "name": "carlos olivero",
            "option": "ensalada cesar",
            "customization": "con mucha salsa",
            "created_at": "2021-08-25 22:36:05"
        },
        "message": "order has been created successfully"
   }
   ```  
* Error Response:

  * code: 400
   ```json
   {
    "success": false,
    "code": 400,
    "data": {},
    "message": "ValueError",
    "errors": {
        "customization": [
            "empty values not allowed"
        ],
        "optionId": [
            "must be of integer type"
        ]
    }
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
    "errors": "Invalid Token"
  }
  ```
  
  or
  
  * code: 403
   ```json
   {
      "detail": "The access method is not allowed"
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
 
  **Only the users with employed type can call this method**