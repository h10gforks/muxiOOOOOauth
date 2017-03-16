# 注册API

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/register/ | 无 | POST |

<hr/>

### URL Params

    无

### POST Data(json)

    {
      "username": "xxxx", // 用户名
      "email": "xxxx@xxxx.com", // 邮箱
      "password": "xxxx" // 密码
    }

### Return Data(json)

    {}


### Status Code:

    201 OK
    400 用户名或邮箱重复
    502 服务器端错误

### Notes
