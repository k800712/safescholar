const MapModule = (function() {
    const DEFAULT_COORDS = { lat: 37.566826, lng: 126.9786567 };
    const MAP_LEVEL = 3;
    const API_ENDPOINT = '/api/nearby_bus_stops';

    let map;

    function init() {
        const mapContainer = document.getElementById('map');
        const mapOption = { 
            center: new kakao.maps.LatLng(DEFAULT_COORDS.lat, DEFAULT_COORDS.lng),
            level: MAP_LEVEL
        };

        map = new kakao.maps.Map(mapContainer, mapOption);
        initializeUserLocation();
    }

    function initializeUserLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(handleLocationSuccess, handleLocationError);
        } else {
            handleLocationError('Geolocation is not supported by this browser.');
        }
    }

    function handleLocationSuccess(position) {
        const { latitude: lat, longitude: lng } = position.coords;
        const userLocation = new kakao.maps.LatLng(lat, lng);
        
        displayMarker(userLocation);
        searchNearbyBusStops(lat, lng);
    }

    function handleLocationError(error) {
        console.error('Error getting user location:', error);
        displayMarker(new kakao.maps.LatLng(DEFAULT_COORDS.lat, DEFAULT_COORDS.lng));
    }

    function displayMarker(location) {
        const marker = new kakao.maps.Marker({ map, position: location });
        map.setCenter(location);
    }

    async function searchNearbyBusStops(lat, lng) {
        try {
            const response = await fetch(`${API_ENDPOINT}?lat=${lat}&lon=${lng}`);
            if (!response.ok) throw new Error('Failed to fetch nearby bus stops');
            const data = await response.json();
            displayBusStops(data);
        } catch (error) {
            console.error('Error fetching nearby bus stops:', error);
        }
    }

    function displayBusStops(stops) {
        stops.forEach(stop => {
            const markerPosition = new kakao.maps.LatLng(stop.y, stop.x);
            const marker = new kakao.maps.Marker({ position: markerPosition });
            marker.setMap(map);
        });
    }

    return { init };
})();

document.addEventListener('DOMContentLoaded', MapModule.init);
