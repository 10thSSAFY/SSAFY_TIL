# Authentication System

## 대체하기
```py
# accouts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
```
```py
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```
```py
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
# Login

## AuthenticationForm():
- 로그인 인증에 사용할 데이터를 입력받는 built-in form

## 로그인 페이지 작성
```py
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
  if request.methd == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('articles:index')
  else:
    form = AuthenticationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/login.html', context)
```

# Login

## 로그아웃 로직 작성
```py
# accounts/views.py

from django.contrib.auth import logout as auth_logout

def logout(request):
  auth_logout(request)
  return redirect('articles:index')
```

# Template with Authentication data

## 현재 로그인 되어있는 유저 정보 출력하기
```html
<!-- articles/index.html -->

<h3>Hello, {{ user.username }}</h3>
```

# 회원가입

## UserCreationForm()
- 회원 가입시 사용자 입력 데이터를 받을 built-in ModelForm

## 회원 가입 페이지 작성 (Error 발생)
```py
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = UserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```

## !!!서술형 예상 문제!!!
```
회원 가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문이다.
커스텀 유저 모델을 사용하려면 Form을 다시 작성해야 한다.
```


## 회원 가집 로직 작성
```py
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
```

## 회원 가입 페이지 작성 (Error 해결)
```py
# accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserCreationForm()
  contenxt = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```

# 회원 탈퇴

## 회원 탈퇴 로직 작성
```py
# accounts/views.py

def delete(request):
  request.user.delete()
  return redirect('articles:index')
```

# 회원정보 수정
- User 객체를 Update 하는 과정

## UserChangeForm()
- 회원정보 수정 시 사용자 입력 데이터를 받을 built-in ModelForm

## 회원정보 수정 페이지 작성
```py
# accounts/views.py

from .forms import CustomUserChangeForm

def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/update.html', context)
```

## CostomUserChangeForm 출력 필드 재정의
```py
# accounts/forms.py

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email')
```

# 비밀번호 변경
- 인증된 사용자의 Session 데이터를 Update 하는 과정

## PasswordChangeForm()
- 비밀번호 변경 시 사용자 입력 데이터를 받을 built-in Form

## 비밀번호 변경 페이지 작성
```py
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm

def change_password(request, user_pk):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/change_password.html', context)
```

# 비밀번호 변경 - 세션 무효화 방지하기

## update_session_auth_hash(request, user)
- 암호 변경 시 세션 무효화를 막아주는 함수
  - 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신

## update_session_auth_hasn 적용
```py
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request, user_pk):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/change_password.html', context)
```

# 인증된 사용자에 대한 접근 제한

## 로그인 사용자에 대해 접근을 제한하는 2가지 방법
1. is_autheticated 속성
2. login_required 데코레이터

## is_authenticated
- 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성
  - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성, 비인증 사용자에 대해서는 항상 False

## is_authenticated 적용하기
```html
<!-- articles/index.html -->

{% if request.user.is_authenticated %}
  <p>로그인 상태입니다.</p>
{% else %}
  <p>로그인을 해 주세요.</p>
{% endif %}
```
```py
# accounts/views.py

def login(request):
  if request.user.is_authenticated:
    return redirect('articles:index')
  pass

def signup(request):
  if request.user.is_authenticated:
    return redirect('articles:index')
  pass
```

## login_required
- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
  - 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴

## login_required 적용하기
```py
# articles/views.py

from django.contrib.auth.decorators import login_required


@login_required
def create(request):
  pass

@login_required
def delete(request, article_pk):
  pass

@login_required
def update(request, article_pk):
  pass
```

# 참고

## 회원가입 후 로그인까지 이어서 진행
```py
if form.is_valid():
  user = form.save()
  auth_login(request, user)
  return redirect('articles:index')
```

# N:1

# 개요

## ForeignKey()
- N:1 관계 설정 모델 필드
```py
article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

## ForeinKey(to, on_delete)
- to: 참조하는 모델 class 이름
- on_delete: 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정 (데이터 무결성)

# 관계 모델 참조

## 역참조 사용 예시
- article.comment_set.all()


# 댓글 구현

## 댓글 CREATE 구현
```py
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)
```
```py
# articles/urls.py

urlpatterns = [
  path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```
```py
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm()
  context = {
    'article': article,
    'comment_form': comment_form,
  }
  return render(request, 'articles/detail.html', context)
```
```html
<!-- articles/detahil.html -->

<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_tocken %}
  {{ comment_form }}
  <input type="submit">
</form>
```