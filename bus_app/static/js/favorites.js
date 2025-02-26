const FavoritesModule = (function() {
    function init() {
        initializeFavoriteButtons();
    }

    function initializeFavoriteButtons() {
        const favoriteButtons = document.querySelectorAll('.favorite-button');
        favoriteButtons.forEach(button => {
            button.addEventListener('click', handleFavoriteClick);
        });
    }

    async function handleFavoriteClick() {
        const routeId = this.dataset.routeId;
        const isFavorite = this.classList.contains('is-favorite');

        try {
            const response = await fetch(API_ENDPOINTS.FAVORITES, {
                method: isFavorite ? 'DELETE' : 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrf_token')
                },
                body: JSON.stringify({ route_id: routeId })
            });

            if (!response.ok) throw new Error('Favorite update failed');

            const data = await response.json();
            if (data.message) {
                this.classList.toggle('is-favorite');
                this.textContent = isFavorite ? 'Add to Favorites' : 'Remove from Favorites';
            }
        } catch (error) {
            console.error('Error:', error);
            displayError('즐겨찾기 업데이트에 실패했습니다.');
        }
    }

    return { init };
})();
