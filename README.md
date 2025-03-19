# ejeju_test

이제주몰 자동화 테스트 프로젝트

#### 기능1
- 테스트할 기능 설명
- 담당자

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
- dev 브랜치로 이동
```
git checkout dev
```
- dev 브랜치 최신화
```
git pull origin dev
```

#### 2. 자신의 작업 브랜치에도 반영
- 본인 브랜치로 이동
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
