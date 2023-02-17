from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from onememos.forms import RegisterForm, MemoForm
from onememos.models import OneMemo, Users
from django.contrib.auth.decorators import login_required

# Create your views here.

# 메인화면
def index(request):
    return render(request, 'index.html')

# 회원가입
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() # User DB에 Insert
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password) 
            # authenticate => 유저 정보가 유효 할시 user객체 리턴 / 틀리면 None
            login(request, user)
            return render(request, "index.html")
        else:
            msg = "올바르지 않은 데이터 입니다."
            return render(request, "register.html", {"form": form , "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

# 로그인
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('index')
    else:
        return render(request, 'login.html')


# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('index')



# 메모 목록 가져오기
@login_required
def get_memo(request):
    all_memo = OneMemo.objects.all().order_by("-write_date") # 모든 데이터 조회, 내림차순(-표시) 조회
    return render(request, 'memo_list.html', {'memo_list':all_memo})



# 메모 작성
@login_required
def create_memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("get_memo")
        else:
            form = MemoForm()
        return redirect('creat_memo')
    else:
        form = MemoForm()
        return render(request, 'create_memo.html',{"form": form})
    

# 메모 수정, 삭제
# @login_required
# def change_memo(request,action,memo_id):
#     if request.method == "POST":
#         pass
#     elif 

    

