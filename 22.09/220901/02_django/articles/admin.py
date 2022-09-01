from django.contrib import admin
from .models import Article

admin.site.register(Article)

#관리자 계정 삭제 방법
# python manage.py shell
# from django.contrib.auth.models import User
# User.objects.get(username='admin', is_superuser=True).delete()
