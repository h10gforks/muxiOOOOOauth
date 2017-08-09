# 修改信息API

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/user/ | 登录的header("Basic Base64(email:passwd)") 或 token | PUT |

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
    401 验证错误
    403 没有访问权限
    502 服务器端错误

### Notes
