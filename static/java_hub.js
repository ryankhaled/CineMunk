document.addEventListener("DOMContentLoaded", function() {
    window.onscroll = function() {
        var header = document.querySelector("header");
        if (window.pageYOffset > 50) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    };

    var searchInput = document.querySelector(".search-bar");
    var resultsContainer = document.querySelector(".search-results");
    var resultsList = document.querySelector(".search-results-list");
    var emptyState = document.querySelector(".search-results-empty");

    if (searchInput && resultsContainer && resultsList && emptyState) {
        var searchData = Array.isArray(window.searchData) ? window.searchData : [];

        var renderResults = function(items) {
            resultsList.innerHTML = "";
            if (items.length === 0) {
                emptyState.hidden = false;
                resultsContainer.classList.remove("has-results");
                return;
            }

            emptyState.hidden = true;
            resultsContainer.classList.add("has-results");
            items.forEach(function(item) {
                var listItem = document.createElement("li");
                listItem.className = "search-results-item";
                listItem.textContent = item.name + " (" + item.type + ")";
                resultsList.appendChild(listItem);
            });
        };

        var handleSearch = function() {
            var query = searchInput.value.trim().toLowerCase();
            if (query.length === 0) {
                resultsList.innerHTML = "";
                emptyState.hidden = true;
                resultsContainer.classList.remove("has-results");
                return;
            }

            var filtered = searchData.filter(function(item) {
                return item.name.toLowerCase().includes(query);
            });
            renderResults(filtered.slice(0, 8));
        };

        searchInput.addEventListener("input", handleSearch);
    }
});
