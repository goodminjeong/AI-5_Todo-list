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
5. Request 생성 : 할일등록(POST), 할일조회(GET), 할일수정(PUT), 할일삭제(DELETE), 할일완료(PUT)

## 📌 주요 기능

#### 회원가입 
- http://127.0.0.1:8000/api/users/signup url로 요청 보내기
- email, password, name, gender, age, introduction 필수 입력
- email은 로그인 시 아이디로 사용함
- gender는 male, female, unknown, non-choice 4가지 선택지가 있음
- age는 0부터 120까지의 정수 입력 가능
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/7544295b-0071-42c1-8a1e-ddb341e01128)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/9c18272a-c775-461e-9a80-5577ba05e2a2)

#### 로그인 
- http://127.0.0.1:8000/api/users/login/ url로 요청 보내기
- 로그인 시 JWT Token 생성
- 이메일 또는 비밀번호 잘못 입력 시 로그인 되지 않음
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/dc09c45c-4d2b-4f47-a3aa-34d0a9d553c1)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/dfa2d678-e7df-434c-af4f-35a1fc6570db)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/d1495d18-2320-4e39-b95c-fb519c11a56b)

#### 회원탈퇴
- http://127.0.0.1:8000/api/users/<user_pk>/ url로 요청 보내기
- 로그인한 유저와 탈퇴하려는 유저가 일치하지 않으면 탈퇴되지 않음
- 탈퇴 시 DB에서 유저 정보를 삭제하는 것이 아닌 is_active 필드를 False로 변경함
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/510f02aa-53e8-4ce4-912a-3299a6aa1843)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/582ccdf6-b1d9-4548-9a6f-e5a28fe8e1dc)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/2805c0ad-ade6-46f2-bdfd-29ca10ed338b)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/d1c859d5-ff86-4433-aabf-d016297cc114)

#### 회원정보 조회 및 수정
- http://127.0.0.1:8000/api/users/<user_pk>/ url로 요청 보내기
- 회원 정보는 email, name, gender, age, introduction, last login(시간) 확인 가능함
- email과 last login은 읽기 전용으로 조회됨
- 회원 정보 부분 수정 가능함
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/e1c56cd4-d7a0-47a2-a224-10c170eb24f7)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/056517e4-9d37-4516-9a1e-a424f1c28658)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/df28c081-affd-4f9c-a3f8-989b823a899d)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/82ffc735-577b-4f55-bdb1-cadd1ab4a214)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/7fb5878d-a868-4625-9c11-5862118e0129)

#### 할일 등록 
- http://127.0.0.1:8000/api/lists/ url로 요청 보내기
- input : title(할 일), is_complete(완료 여부)
- output : id, title, is_complete, created_at, updated_at, completion_at(완료 날짜)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/b7165527-de0a-45ab-8262-774f8e2f317c)

#### 할일 조회
- http://127.0.0.1:8000/api/lists/ url로 요청 보내기
- 게시글 pk값, title, is_complete, created_at, updated_at, completion_at 조회
- 내가 작성한 todo list만 조회 가능
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/4aa494ea-68a3-4c82-bb06-e3aadc091fe4)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/9715dc74-84d9-4e96-a8bf-bd96f572b75c)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/cb6f71be-4555-4c17-ae55-8082152776e7)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/e06f850a-2111-4300-95c8-c29de4dc0032)

#### 할일 수정
- http://127.0.0.1:8000/api/lists/<todo_pk>/ url로 요청 보내기
- title만 수정 가능
- 내가 작성한 todo list만 수정 가능
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/bb1401b2-393f-41f4-bed9-adce4c38eac7)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/3a00e38f-0d32-4088-a531-19ce0f347cf1)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/5f8c6bf3-c78e-483b-8391-a6b74f5c79a5)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/676ab767-37d7-4306-adc0-9888dfc79220)

#### 할일 삭제
- http://127.0.0.1:8000/api/lists/<todo_pk>/ url로 요청 보내기
- 내가 작성한 todo list만 삭제 가능
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/e01a9723-29e1-4ae2-adf1-8849eda4968b)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/a3139457-d52d-4319-9e68-fbc60bcdd6a5)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/ac7527ef-b10f-4826-ab7c-9139b85884f4)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/1b46dba8-a618-466b-a459-52c30c772e1e)

#### 할일 완료
- http://127.0.0.1:8000/api/lists/<todo_pk>/complete/ url로 요청 보내기
- 내가 작성한 todo list만 완료 체크 가능
- 할일 완료되면 completion_at 필드에 오늘 날짜 입력됨
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/2bab2334-e77c-4c01-9adb-55c763896b2f)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/49bfe3de-3587-40d8-9119-92b319b8a6b6)
![image](https://github.com/goodminjeong/AI-5_Todo-list/assets/125722304/9b6f49f0-32d7-46c4-8193-f8122559467a)
