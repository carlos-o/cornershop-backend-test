# Documentation of services module Menu
### Table of contents
* **[Menu](#Menu)**<br>

## Menu
### List Menu 
**TOKEN IS REQUIRED**

list with all menu create for specific user

* Url

  http://127.0.0.1:8000/menu

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
        "count": 2,
        "countItemsOnPage": "20",
        "current": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name": "menu del dia miercoles",
                "description": "dia de ensalada",
                "start_date": "2021-08-25",
                "created_at": "2021-08-24 01:26:55",
                "options": []
            },
            {
                "id": 1,
                "name": "menu del dia lunes",
                "description": "el mejor menu de las semana",
                "start_date": "2021-08-23",
                "created_at": "2021-08-23 23:29:30",
                "options": [
                    {
                        "id": 1,
                        "description": "Pasta con carne y pan",
                        "created_at": "2021-08-24 00:29:49"
                    },
                    {
                        "id": 2,
                        "description": "ensalada cesar",
                        "created_at": "2021-08-24 00:30:19"
                    },
                    {
                        "id": 3,
                        "description": "sopa de porotos negros",
                        "created_at": "2021-08-24 00:30:37"
                    }
                ]
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
 
  **only admin user has permission to call this method**
 
 
### Get Menu
**TOKEN IS REQUIRED**

get specific menu

* Url

  http://127.0.0.1:8000/menu/menu_id/
  

* Method

  **GET**

* Url Params

  **menu_id** id of menu

* Data Params

  **None**

* Success Response:
   * code: 200
   ```json
    {
        "success": true,
        "code": 200,
        "data": {
            "id": 1,
            "name": "menu del dia lunes",
            "description": "el mejor menu de las semana",
            "start_date": "2021-08-23",
            "created_at": "2021-08-23 23:29:30",
            "options": [
                {
                    "id": 1,
                    "description": "Pasta con carne y pan",
                    "created_at": "2021-08-24 00:29:49"
                },
                {
                    "id": 2,
                    "description": "ensalada cesar",
                    "created_at": "2021-08-24 00:30:19"
                },
                {
                    "id": 3,
                    "description": "sopa de porotos negros",
                    "created_at": "2021-08-24 00:30:37"
                }
            ]
        },
        "message": "ok"
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
    "errors": "Account blocked, contact the administrators."
  }
  ```
  
  or
  
  * code: 404
  ```json
  {
    "success": true,
    "code": 404,
    "data": {},
    "message": "Not found.",
    "errors": {
        "error": "Not found."
    }
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

### Create Menu
**TOKEN IS REQUIRED**

Create a new menu

* Url

  http://127.0.0.1:8000/menu/

* Method

  **POST**

* Url Params

  **None**

* Data Params
    
    * description param is optional
    ```json
    {
      "name": "menu del dia jueves",
      "description": "dia de lasaña :D", 
      "start_date": "2021-08-24"
    }
    ```

* Success Response:
   * code: 200
   ```json
  {
    "success": true,
    "code": 201,
    "data": {
        "id": 4,
        "name": "menu del dia viernes",
        "description": null,
        "start_date": "2021-08-27",
        "created_at": "2021-08-25 23:40:39",
        "options": []
    },
    "message": "menu has been created successfully"
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
        "description": [
            "empty values not allowed"
        ],
        "name": [
            "empty values not allowed"
        ],
        "start_date": [
            "empty values not allowed"
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
 
  **only admin user has permission to call this method**
 
### Update Menu
**TOKEN IS REQUIRED**

update a specific menu

* Url

  http://127.0.0.1:8000/menu/menu_id/

* Method

  **PUT**

* Url Params

  **menu_id** id of menu

* Data Params

    ```json
    ```

* Success Response:
   * code: 200
   ```json
  {
    "success": true,
    "code": 200,
    "data": {
        "id": 4,
        "name": "menu del dia viernes",
        "description": null,
        "start_date": "2021-08-27",
        "created_at": "2021-08-25 23:40:39",
        "options": []
    },
    "message": "menu has been updated successfully"
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
        "description": [
            "empty values not allowed"
        ],
        "name": [
            "empty values not allowed"
        ],
        "start_date": [
            "empty values not allowed"
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
    "errors": "Account blocked, contact the administrators."
  }
  ```
  
  or
  
  * code: 404
  ```json
  {
    "success": true,
    "code": 404,
    "data": {},
    "message": "Not found.",
    "errors": {
        "error": "Not found."
    }
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

### Create option
**TOKEN IS REQUIRED**

create a option to specific menu

* Url

  http://127.0.0.1:8000/menu/menu_id/option/

* Method

  **POST**

* Url Params

  **menu_id** id of menu

* Data Params

    ```json
    {
      "description": "sopa de porotos negros con chorizo"
    }
    ```

* Success Response:
   * code: 201
   ```json
    {
    "success": true,
    "code": 201,
    "data": {
        "id": 5,
        "description": "sopa de porotos negros con chorizo",
        "created_at": "2021-08-25 23:50:36"
    },
    "message": "options has been added successfully"
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
        "description": [
            "empty values not allowed"
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
    "errors": "Account blocked, contact the administrators."
  }
  ```
  
  or
  
  * code: 404
  ```json
  {
    "success": true,
    "code": 404,
    "data": {},
    "message": "Not found.",
    "errors": {
        "error": "Not found."
    }
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


### Update option
**TOKEN IS REQUIRED**

update a option to specific menu

* Url

  http://127.0.0.1:8000/menu/menu_id/option/option_id/

* Method

  **PUT**

* Url Params

  **menu_id** id of menu
  
  **option_id** id of option

* Data Params

    ```json
    {
      "description": "sopa de porotos negros con chorizo"
    }
    ```

* Success Response:
   * code: 200
   ```json
  {
    "success": false,
    "code": 400,
    "data": {},
    "message": "ValueError",
    "errors": {
        "description": [
            "empty values not allowed"
        ]
     }
   }
   ```  
* Error Response:
   
  * code: 400
   ```json
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
  
  * code: 404
  ```json
  {
    "success": true,
    "code": 404,
    "data": {},
    "message": "Not found.",
    "errors": {
        "error": "Not found."
    }
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

### Delete option
**TOKEN IS REQUIRED**

delete a option to specific menu

* Url

  http://127.0.0.1:8000/menu/menu_id/option/option_id/

* Method

  **DELETE**

* Url Params

  **menu_id** id of menu
  
  **option_id** id of option

* Data Params

  **None**

* Success Response:
   * code: 200
   ```json
   {
    "success": true,
    "code": 200,
    "data": {},
    "message": "options has been delete successfully"
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
    "errors": "Account blocked, contact the administrators."
  }
  ```
  
  or
  
  * code: 404
  ```json
  {
    "success": true,
    "code": 404,
    "data": {},
    "message": "Not found.",
    "errors": {
        "error": "Not found."
    }
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

### Send Reminder
**TOKEN IS REQUIRED**

* Url

  http://127.0.0.1:8000/menu/menu_id/send-reminder/

* Method

  **GET**

* Url Params

  **menu_id** id of menu

* Data Params

  **None**

* Success Response:
   * code: 200
   ```json
   {
    "success": true,
    "code": 200,
    "data": {},
    "message": "The reminder has sent correctly"
   }
   ```  
* Error Response:
  
  * code: 400 menu without options
   ```json
  {
    "success": false,
    "code": 400,
    "data": {},
    "message": "is not possible send message, please add options first.",
    "errors": ""
  }
   ``` 
  or
  
  * code: 400 The reminder was sent previously
   ```json
  {
    "success": false,
    "code": 400,
    "data": {},
    "message": "The reminder was sent previously, it cannot be sent again.",
    "errors": ""
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
  
  * code: 404
  ```json
  {
    "success": true,
    "code": 404,
    "data": {},
    "message": "Not found.",
    "errors": {
        "error": "Not found."
    }
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