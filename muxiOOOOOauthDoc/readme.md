# muxiOOOOOauth API DOC

### Environment Config

```
C_FORCE_ROOT:(true) Celery work with root privilege
CELERY_ACCEPT_CONTENT:(json)Celery accepted content type
CELERY_TASK_SERIALIZER: (json)Celery task serializer type
AUTH_MAIL_USERNAME: Confirm Email sender
AUTH_MAIL_PASSWORD: Confirm Email sender's password
AUTH_SQLALCHEMY_DATABASE_URI: database URI for muxiOOOOOauth
REDIS_BROKER_HOSTNAME: (redis1 for dev, redis1.muxiauth.svc.cluster.local for production)Hostname for redis broker
REDIS_BACKEND_HOSTNAME: (redis2 for dev, redis2.muxiauth.svc.cluster.local for production)Hostname for redis backend
```
