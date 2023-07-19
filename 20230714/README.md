# TIL
## 2023-07-13
### 마크다운(Markdown)
- [마크다운 간단 활용](https://sirupe.github.io/first-posting/)
___
### CLI 문법 및 활용

- 기초 문법 실습
    | CLI 기초 문법 | 역할
    |:---:|:---
    | `.` | 현재 디렉토리
    | `..` | 현재의 상위 디렉토리(부모 폴더)
    | `touch` | 파일 생성
    | `mkdir` | 새 디렉토리 생성
    | `ls` | 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
    | `cd` | 현재 작업 중인 디렉토리를 변경 (위치 이동)
    | `start` | 폴더/파일을 열기 (Mac에서는 `oepn`을 이용)
    | `rm` | 파일 삭제 (-r 옵션을 사용해 디렉토리 삭제)

- 절대 경로<br>
    - Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
    <br><br>
- 상대 경로<br>
    - 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
___
### git (분산 버전 관리 시스템)
1. git의 역할
    - 코드의 버전(히스토리)를 관리
    - 개발되어 온 과정 파악
    - 이전 버전과의 변경 사항 비교
2. git의 3가지 영역
    1. Working Directory
    <br> - 실제 작업 중인 파일들이 위치하는 영역
    2. Staging Area
    <br> - WorkingDirectory에서 변경된 파일 중,
    <br> 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나
    <br> 제외할 수 있는 중간 준비 영역
    3. Repository
    <br> - 버전 이력과 파일들이 영구적으로 저장되는 영역
    <br> 모든 버전과 변경 이력이 기록됨
    - Commit (버전)
    <br> - 번경된 파일들을 저장하는 행위이며,
    <br> 마치 사진을 찍듯이 기록한다 하여 `snapshot`이라고도 함
3. git의 동작
    - git init
        - 로컬 저장소 설정(초기화)
        - git의 버전 관리를 시작할 디렉토리에서 진행
    - git add `파일(or 경로)이름`
        - 변경사항이 있는 파일을 staging area에 추가
    - git commit
        - staging area에 있는 파일들을 저장소에 기록<br>
        \> 해당 시점의 버전을 생성하고 변경 이력을 남기는 것<br>
        ex) git commit -m "`기록하고자 하는 메시지`"
    - git config --global user.email "`메일주소`"
    - git config --global user.name "`유저네임`"<br>
        \> commit 작성자(author) 설정<br>
        \> (global로 설정 후 앞으로 재입력 하지 않음)
    - git은 로컬 저장소 내 모든 파일의 <span style='color:red;'>'변경사항'</span>을 감시하고 있다.
    > git commit 실습
    >> 1. 바탕화면에 git_commit 폴더를 만들고 git 저장소 생성
    >> 2. 해당 폴더 안에 a.txt라는 텍스트 파일을 만들고, "add a.txt"라는 커밋 메세지로 커밋 생성
    >> 3. 이번에는 b.txt라는 텍스트 파일을 만들고, "add b.txt"라는 커밋 메세지로 커밋 생성
    >> 4. a.txt 파일을 수정하고, "updata a.txt"라는 커밋 메세지로 커밋 생성
    >> 5. 커밋 목록 확인

    > git commit 풀이 (CLI 버전)
    >> 1. mkdir git_commit<br>
    >> cd git_commit<br>
    >> git init<br>
    >> 2. touch a.txt<br>
    >> git add .<br>
    >> git commit -m "`create a.txt`"<br>
    >> 3. touch b.txt<br>
    >> git add .<br>
    >> git commit -m "`create b.txt`"<br>
    >> 4. git add .<br>
    >> git commit -m "`edited a.txt`"<br>
    >> 5. git status<br>
    >> git log

    
### 참고
#### 로컬(local)
- 현재 사용자가 직접 접속하고 있는 기기 또는 시스템<br>
개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조작하는 환경
#### git 기타 명령어
- <span style='color:red;'>git status</span>
    - <span style='color:red;'>현재 로컬 저장소의 팡리 상태 보기</span>
- git log
    - commit history 보기
- git log --oneline
    - commit 목록 한 줄로 보기
- git config --global -l
    - git global 설정 정보 보기
#### git init 주의사항
- git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것
- 즉, 이미 git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것
- git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git 저장소의 변경사항을 추적할 수 없기 때문
### Romote Repository
#### 원격 저장소
코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
##### 다양한 원격 저장소
- GitLab
- GitHub
- Bitbucket
### 로컬 & 원격 저장소
#### git과 github
##### 사전 준비
1. 공용 문서 안내에 따라 github 가입 및 설정 진행
2. github repository 생성

<span style='color:red;'>git remote</span> add origin remote_repo_url<br>
로컬 저장소에 원격 저장소 주소 추가<br>
git remote add <span style='color:blue;'>origin</span> remote_repo_url<br>
추가하는 원격 저장소 별칭

##### git remote
- 원격 저장소 등록
    - git remote add origin `페이지 URL`
- 추가된 원격 저장소 목록 확인
    - git remote -v
- push / pull & clone
    - <span style='color:red;'>git push</span> -u orgin master
    - 원격 저장소에 commit 목록을 업로드
#### git push
- commit 목록 업로드
- 최초 push시에는 github으로 부터 인증서(git credential) 발급이 필요
- 해당 원격 저장소에 push할 수 있는 권한이 있는지 확인하기 위함
- github 로그인
- 터미널 메시지 확인
- 원격 저장소에 잘 push 되었는지 확인
#### 원격 저장소에는 commit이 올라가는 것
- commit 이력이 없다면 push 할 수 없다.
- git pull origin master
    - 원격 저장소의 변경사항만을 받아옴(업데이트)
- git clone `페이지url`
- ~~git remote rm origin (지우기)~~

### gitigore
Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일
- 프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문
#### gitignore 예시
> 1. .gitignore 파일 생성 (파일명 앞에 `.`입력, 확장자 없음)
> 2. a와 b 이름을 가진 텍스트 파일 생성
> 3. gitignore에 a.txt 작성
> 4. git init
> 5. git status
### gitignore 주의사항
이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음
- gitignore 설정 서비스
    - 운영체제, 프레임워크, 프로그래밍 언어 등 개발 환경에 따라 gitignore 목록을 만들어주는 사이트
    - https://www.toptal.com/developers/gitignore/
### github 활용
#### 포트폴리오
githugb은 어디에 활용할까
1. 프로젝트 협업
2. 개인 포틀폴리오
#### github 활용처
1. TIL을 통해 내가 학습하는 것을 기록
2. 개인, 팀 프로젝트 코드를 공유
    - 개발 면접 지원 시 본인의 github 주소를 공유해 어떤 프로젝트들을 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용
3. 오픈 소스 프로젝트에 기여
#### TIL
Today I Learned

매일 내가 배운 것을 마크다운으로 정리해서 문서화 하는 것
- 단순히 배운 것 만을 필기하는 것이 아닌 스스로 더 나아가 어떤 학습을 했는지를 기록하는 것
#### '문서화'의 중요성
신입 개발자에게 요구되는 가장 중요한 덕목
- 꾸준히 스스로 학습해 성장할 수 있고 문서화를 통해 내 생각을 정리하고 팀에게 공유할 수 있는 능력
#### 실습1 - TIL 만들기
1. TIL이라는 이름의 Github Repository 생성
2. 로컬 저장소 설정
3. README.md 생성 및 지금까지의 수업 내용을 정리하고 commit을 생성
4. TIL 원격 저장소를 추가
5. commit 목록을 push
#### 실습2 - Github Profile 꾸미기
1. 본인의 github username으로 Github Repository를 생성
2. 로컬 저장소 설정
3. README.md 파일을 생성하고, 해당 파일에 자유롭게 자기 소개를 작성
4. commit생성, remote 및 push
5. https://github.com/`내유저네임`으로 접속 후 내 프로필 모습 확인
6. github profile을 꾸미는 방법을 추가적으로 구글링 해보기

## 참고
### git 기타 명령어
- git remote -v
    - 현재 로컬 저장소에 등록된 원격 저장소 목록 보기
- git remote rm `원격_저장소_이름`
    - 현재 로컬 저장소에 등록된 원격 저장소 삭제