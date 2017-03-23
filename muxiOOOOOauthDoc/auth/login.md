# 登录API

> 对应应用首页的登录

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/login/ | 登录header | GET |

<hr/>

### URL Params

    无

### POST Data(json)

    无

### Return Data(json)

    {
      "uid": 1 // 用户的id
    }


### Status Code:

    200 OK
    401 用户名和密码错误
    403 禁止访问, 用户验证出错
    502 服务器端错误

### Notes
