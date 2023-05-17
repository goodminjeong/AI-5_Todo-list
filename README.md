# Django-rest-framework-Project-TodoList(Backend only)
DRF를 이용한 Todo List 백엔드 기능 구현

## 🖥️ 프로젝트 소개
DRF를 사용하여 유저와 할일목록의 생성, 조회, 수정 삭제(CRUD) API를 만들었습니다.

## 🕰️ 개발 기간
* 23.04.26 - 23.04.28

### ⚙️ 개발 환경
- `Python 3.11`
- **IDE** : visual studio code
- **Framework** : Django-Rest-Framework
- **Database** : sqllite3
- 그외 : **requirements.txt** : requirements.txt 참조

### 🔑 프로젝트 설치 및 실행 방법

#### 깃허브 클론하기
- git init
- git clone git@github.com:goodminjeong/AI-5_Todo-list.git
#### 패키지 밎 라이브러리 설치
- pip install -r requirements.txt
#### 서버 실행
- python manage.py runserver
#### 포스트맨 실행
1. workspace 생성
2. collection 생성 : users
3. Request 생성 : signup(POST), login(POST), logout(POST), refresh(POST), user delete(DELETE), profile(GET), profile update(PUT)
4. collection 생성 : Todo-list
5. Request 생성 : 할일등록(POST), 할일조회(GET), 할일수정(PUT), 할일삭제(DELETE)

## 📌 주요 기능

#### 회원가입 
- http://127.0.0.1:8000/api/users/signup url로 요청 보내기
- email, password, name, gender, age, introduction 필수 입력
- email은 로그인 시 아이디로 사용함
- gender는 male, female, unknown, non-choice 4가지 선택지가 있음
- age는 0부터 120까지의 정수 입력 가능

#### 로그인 
- http://127.0.0.1:8000/api/users/login/ url로 요청 보내기
- 로그인 시 JWT Token 생성

#### 회원탈퇴
- http://127.0.0.1:8000/api/users/<user_pk>/ url로 요청 보내기
- .delete() 메서드로 DB에서 유저 정보 삭제

#### 회원정보 조회 및 수정
- http://127.0.0.1:8000/api/users/<user_pk>/ url로 요청 보내기
- 회원 정보는 email, name, gender, age, introduction, last login(시간) 확인 가능함
- email과 last login은 읽기 전용으로 조회됨
- 회원 정보 부분 수정 가능함

#### 할일 등록 
- http://127.0.0.1:8000/api/lists/ url로 요청 보내기
- input : title(할 일), is_complete(완료 여부)
- output : title, is_complete, completion_at(완료 날짜)

#### 할일 조회
- http://127.0.0.1:8000/api/lists/ url로 요청 보내기
- 게시글 pk값, title, is_complete, created_at, updated_at, completion_at 조회
- 내가 작성한 todo list만 조회 가능

#### 할일 수정
- http://127.0.0.1:8000/api/lists/<todo_pk>/ url로 요청 보내기
- title, is_complete, completion_at 수정 가능
- 원래 is_complete가 true가 되면 그때 날짜를 completion_at에 저장하려고 하였으나 구현하지 못 함
- 내가 작성한 todo list만 수정 가능

#### 할일 삭제
- http://127.0.0.1:8000/api/lists/<todo_pk>/ url로 요청 보내기
- 내가 작성한 todo list만 삭제 가능
