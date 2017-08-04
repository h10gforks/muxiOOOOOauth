# 获取信息API

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/user/ | 无 | GET |

<hr/>

### URL Params

    email: xxx@xx.com // Email

### POST Data(json)

    无

### Return Data(json)

    {  
        "email": "xxx@xx.com",
        "id": 111,
        "phone": null,
        "qq": null,
        "school": null,
        "sid": null, // 学号
        "username": "xxx"
    } // 用户信息json

### Status Code:

    200 OK
    404 没有找到用户
    502 服务器端错误

### Notes
