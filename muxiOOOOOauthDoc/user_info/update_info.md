# 修改信息API

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/user/ | 登录的header | PUT |

<hr/>

### URL Params

    无

### POST Data(json)

    {  
        "phone": "xxx",
        "qq": "xxx",
        "school": "xxx",
        "sid": "xxx", // 学号
        "username": "xxx"
    } 

### Return Data(json)

    无

### Status Code:

    200 OK
    401 邮箱密码错误
    403 没有访问权限
    502 服务器端错误

### Notes
