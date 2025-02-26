document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const autocompleteResults = document.getElementById('autocomplete-results');

    searchInput.addEventListener('input', function() {
        const query = this.value;
        if (query.length > 2) {
            fetch(`/autocomplete?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    autocompleteResults.innerHTML = '';
                    data.forEach(item => {
                        const li = document.createElement('li');
                        li.textContent = item;
                        li.addEventListener('click', function() {
                            searchInput.value = this.textContent;
                            autocompleteResults.innerHTML = '';
                        });
                        autocompleteResults.appendChild(li);
                    });
                });
        } else {
            autocompleteResults.innerHTML = '';
        }
    });
});
