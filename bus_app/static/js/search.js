// 상수 정의
const API_ENDPOINTS = Object.freeze({
    AUTOCOMPLETE: '/api/autocomplete',
    BUS_STOP: '/search/bus_stop',
    BUS_ROUTE: '/search/bus_route'
});

const DEFAULT_COORDS = Object.freeze({ latitude: 37.566826, longitude: 126.978652 }); // 서울시청 좌표 (기본값)

const ERROR_MESSAGES = Object.freeze({
    AUTOCOMPLETE_FAIL: '자동완성 데이터를 가져오는데 실패했습니다.',
    SEARCH_FAIL: '검색 중 오류가 발생했습니다.',
    NO_RESULTS: '검색 결과가 없습니다.'
});

const DEBOUNCE_DELAY = 300; // ms
const MIN_QUERY_LENGTH = 2;

// 모듈 패턴을 사용한 캡슐화
const BusSearchModule = (function() {
    let searchInput, suggestionsList, searchResults, debounceTimer;

    function init() {
        initializeElements();
        addEventListeners();
    }

    function initializeElements() {
        searchInput = document.getElementById('search-input');
        suggestionsList = document.getElementById('suggestions');
        searchResults = document.getElementById('search-results');
    }

    function addEventListeners() {
        searchInput.addEventListener('input', handleInput);
        searchInput.addEventListener('keydown', handleKeydown);
        suggestionsList.addEventListener('click', handleSuggestionClick);
        document.getElementById('bus-stop-btn').addEventListener('click', () => performSearch('stop'));
        document.getElementById('bus-route-btn').addEventListener('click', () => performSearch('route'));
    }

    function handleInput() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            const query = searchInput.value;
            if (query.length > MIN_QUERY_LENGTH) {
                fetchAutocomplete(query);
            } else {
                clearSuggestions();
            }
        }, DEBOUNCE_DELAY);
    }

    // ... (나머지 함수들은 그대로 유지)

    function clearSuggestions() {
        suggestionsList.innerHTML = '';
    }

    // 검색 결과 표시 함수 개선
    function displayResults(data) {
        if (data.documents.length === 0) {
            searchResults.innerHTML = `<p>${ERROR_MESSAGES.NO_RESULTS}</p>`;
            return;
        }
        searchResults.innerHTML = data.documents.map(createResultItem).join('');
    }

    function createResultItem(item) {
        return `
            <div class="result-item">
                <h3>${item.place_name}</h3>
                <p>${item.address_name}</p>
                <p>거리: ${item.distance}m</p>
            </div>
        `;
    }

    // ... (나머지 함수들은 그대로 유지)

    return { init };
})();

document.addEventListener('DOMContentLoaded', BusSearchModule.init);
