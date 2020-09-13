学习笔记

###### 11. DjangoWeb相关功能-表单

```
<form>
username	
password
</form>
```

使用form对象定义表单

\#from.py

From Django import forms

###### 12. DjangoWeb相关功能-表单CSRF防护

在表单里添加 {%csrf_token%}

Setting.py 里面csrf 中间件实现

###### 13. DjangoWeb相关功能-用户管理认证

###### 14. DjangoWeb相关功能-信号

独立程序之间的交互

###### 15. DjangoWeb相关功能-中间件

- 全局改变输入输出，轻量级，低级的插件系统对请求，响应处理的钩子框架

###### 16. Django相关功能-生产环境部署

- gunicorn 比nginx 性能高
- Pip install  gunicorn  
- Gunicorn  mydjango.wsgi
- \17. Django相关功能-celery介绍
- 定时任务，celery ：分布式消息队列
- \18. Django相关功能-celery定时任务的实现
- \19. Flask上下文与信号