# 버스 정보 검색 애플리케이션

이 애플리케이션은 사용자가 버스 정류장과 노선 정보를 쉽게 검색하고 관리할 수 있도록 도와주는 웹 기반 서비스입니다.

## 주요 기능

- 카카오 로그인을 통한 사용자 인증
- 버스 정류장 및 노선 검색 (자동완성 기능 포함)
- 지도에서 현재 위치 및 주변 버스 정류장 표시
- 버스 노선 즐겨찾기 기능
- 반응형 웹 디자인

## 기술 스택

- Backend: Flask
- Frontend: HTML, CSS, JavaScript
- 데이터베이스: SQLAlchemy (SQLite)
- 캐싱: Redis
- 지도 API: Kakao Maps API
- 인증: Kakao OAuth

## 설치 및 실행 방법

1. 저장소 클론
git clone git@github.com:k800712/safescholar.git
cd bus_app


2. 가상 환경 생성 및 활성화
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate



3. 의존성 설치
pip install -r requirements.txt



4. 환경 변수 설정
`.env` 파일을 생성하고 다음 변수들을 설정하세요:
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
KAKAO_CLIENT_ID=your_kakao_client_id
KAKAO_REDIRECT_URI=http://localhost:5000/oauth



5. 데이터베이스 초기화
`flask db upgrade`



6. 애플리케이션 실행
`flask run`



7. 브라우저에서 `http://localhost:5000`으로 접속



## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
