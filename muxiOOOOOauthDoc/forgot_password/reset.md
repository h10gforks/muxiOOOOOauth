# 修改密码API

| URL | Header |  Method |
| ------------- |:-------------:| -----:|
| /api/forgot_password/reset/ | 无 | POST |

<hr/>

### URL Params

    无

### POST Data(json)

    {
        "email": "xxxxxx@xxxx.com",   // string, 用户邮箱
        "new_password": "xxxxxxxxxxx" // string, 新密码
        "captcha": "4444"             // string, 验证码
    }

### Return Data(json)

    无

### Status Code:

    200 OK
    404 没有找到用户
    403 用户验证错误
    502 服务器端错误

### Notes
