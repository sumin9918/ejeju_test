# 🍊 ejeju_test

이제주몰 자동화 테스트 프로젝트

#### 로그인/미로그인 검색, 카테고리 진입
1. 로그인 상태로 상품 검색
2. 미로그인 상태로 상품 검색
3. 로그인/미로그인 검색 목록 비교
4. 헤더 카테고리 진입
- 김동연

#### 기능2
- 테스트할 기능 설명
- 담당자

#### 기능3
- 테스트할 기능 설명
- 담당자

#### 기능4
- 테스트할 기능 설명
- 담당자


## 📅 진행기간
- 2025.03.17 - 2025.03.18

## 📋 환경정보
<img src="https://img.shields.io/badge/Google%20Chrome%20134ver-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white">
<img src="https://img.shields.io/badge/Windows%2010-0078D6?style=for-the-badge&logo=windows&logoColor=white">

## 🔧 사용기술
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white">
<img src="https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3">

## Git을 최신상태로 유지
- 팀원이 pr을 보냈을 때 어떻게 해야 할까요?

#### 1. dev 브랜치를 최신 상태로 유지
##### 방법1 깃 명령어 이용
- dev 브랜치로 이동
```
git checkout dev
```
- dev 브랜치 최신화
```
git pull origin dev
```
##### 방법2 깃헙 데스크탑 이용
1. 깃헙 데스크탑을 킨다
2. 현재 브랜치를 dev로 이동한다
3. fetch origin -> pull origin

- **주의점** : 현재 작업물이 있으면 브랜치를 이동할 수 없습니다. 그러니 commit을 하거나 혹은 add를 한 상태로 브랜치를 이동해 주세요.
  - 만약 경고를 무시하고 브랜치를 이동하면 커밋시키지 않은 작업물은 사라집니다!!

#### 2. 자신의 작업 브랜치에도 반영
- 본인 브랜치로 이동 (현재 본인 브랜치에 있다면 생략)
```
git checkout 본인 브랜치
```
- dev에서 변경된 내용 반영
```
git merge dev
```

#### 만약 내 파일과 충돌이 발생했다면?
- 팀원과 완만히 합의 후, commit

## 브런치
- 로컬 브랜치 : 내 컴퓨터에 있는 브랜치
- 원격 브랜치 : github에 있는 브랜치

#### 브랜치 이동
```
git checkout 이동할 브랜치명
```

#### 브랜치 삭제법
- 반드시 변경 사항이 없을 때에만 하세요

- 먼저 dev 브랜치 이동
```
git checkout dev
```
- 로컬 브랜치 삭제
```
git branch -d 브랜치명
git branch -D 브랜치명 # 강제 삭제
```
- 원격 브랜치 삭제
```
git push origin --delete 브랜치명
```

#### 브랜치 조회
- 로컬 브랜치 목록 확인
```
git branch
```
- 원격 브랜치 목록 확인
```
git branch -r
```

#### 브랜치 생성법
```
git checkout -b 새로운 브랜치명
```


## Commit Conventions
| Message  | Description                   |
| -------- | ----------------------------- |
| fix      | fixed bugs and errors         |
| feat     | added new feature             |
| refactor | updated existing feature/code |
| docs     | added/updated docs            |
| img      | added/updated images          |
| init     | added initial files           |
| ver      | updated version               |
| chore    | add library                   |
