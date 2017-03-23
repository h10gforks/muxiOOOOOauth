# 获取验证码API

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/forgot_password/get_captcha/ | 无 | POST |

<hr/>

### URL Params

    无

### POST Data(json)

    {
      "username": "kasheemlew" // string, 用户名用于邮件显示，选填
      "email": "xxx@xxxx.com"  // string, 获取验证码的邮箱
    }

### Return Data(json)

    {
      "token": "xxxxxxxx" // string, 重置密码时要提交的token
      "captcha": "4444" // string, 四位验证码
    }


### Status Code:

    200 OK
    404 没有找到用户
    502 服务器端错误

### Notes
