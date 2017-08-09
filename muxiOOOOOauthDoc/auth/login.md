# 登录API

> 对应应用首页的登录

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/login/ | 登录header("Basic Base64(username:passwd)") | GET |

<hr/>

### URL Params

    无

### POST Data(json)

    无

### Return Data(json)

    {
      "uid": 1, // 用户的id
      "token": "dafjslkfljfiasjjOJFOJDIOFJ" // 用户的token, 有效时间60*60秒
    }


### Status Code:

    200 OK
    401 用户名和密码错误
    403 无访问权限
    502 服务器端错误

### Notes
