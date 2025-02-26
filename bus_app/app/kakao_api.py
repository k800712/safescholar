import requests

KAKAO_API_KEY = 'YOUR_KAKAO_API_KEY'

def get_bus_location(bus_id):
    # 이 함수는 실제 카카오 API를 호출하여 버스 위치를 가져옵니다.
    # 실제 구현은 카카오 API 문서를 참조하여 작성해야 합니다.
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={bus_id}"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    # 여기서는 간단한 예시로 고정된 위치를 반환합니다.
    return {"lat": 37.566826, "lng": 126.9786567}
