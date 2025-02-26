const FavoritesModule = (function() {
    const BUTTON_TEXT = {
        ADD: 'Add to Favorites',
        REMOVE: 'Remove from Favorites'
    };

    const API_ENDPOINT = '/api/favorites';

    function init() {
        document.querySelectorAll('.favorite-button').forEach(button => {
            button.addEventListener('click', handleFavoriteClick);
        });
    }

    async function handleFavoriteClick(event) {
        const button = event.currentTarget;
        const routeId = button.dataset.routeId;
        const isFavorite = button.classList.contains('is-favorite');

        try {
            const response = await updateFavoriteStatus(routeId, isFavorite);
            if (response.message) {
                updateButtonState(button, !isFavorite);
            }
        } catch (error) {
            console.error('Error updating favorite status:', error);
        }
    }

    async function updateFavoriteStatus(routeId, isFavorite) {
        const response = await fetch(API_ENDPOINT, {
            method: isFavorite ? 'DELETE' : 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrf_token')
            },
            body: JSON.stringify({ route_id: routeId })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return response.json();
    }

    function updateButtonState(button, isFavorite) {
        button.classList.toggle('is-favorite', isFavorite);
        button.textContent = isFavorite ? BUTTON_TEXT.REMOVE : BUTTON_TEXT.ADD;
    }

    function getCookie(name) {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith(name + '='));
        return cookieValue ? decodeURIComponent(cookieValue.split('=')[1]) : null;
    }

    return { init };
})();

document.addEventListener('DOMContentLoaded', FavoritesModule.init);
