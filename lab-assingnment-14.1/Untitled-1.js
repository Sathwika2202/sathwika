// Task: Fetch JSON from API, render item list with loading/error states, and safe DOM manipulation

// Helper function: creates a DOM node with optional text and classes
function createNode(tag, text = '', classNames = []) {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (classNames.length) node.classList.add(...classNames);
    return node;
}

// The main function: fetch and render
function fetchAndRenderList(apiUrl, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Show loading skeleton/text
    container.innerHTML = '';
    const loading = createNode('div', 'Loading items...', ['loading-skeleton']);
    container.appendChild(loading);

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not OK');
            }
            return response.json();
        })
        .then(data => {
            container.innerHTML = '';
            if (!Array.isArray(data) || data.length === 0) {
                container.appendChild(createNode('div', 'No items found.', ['empty-list']));
                return;
            }
            const list = createNode('ul', '', ['item-list']);
            data.forEach(item => {
                // Safe: escape possible untrusted text content
                const li = createNode('li');
                li.textContent = item.name ? String(item.name) : JSON.stringify(item);
                list.appendChild(li);
            });
            container.appendChild(list);
        })
        .catch(error => {
            container.innerHTML = '';
            const errMsg = createNode('div', `Failed to load items: ${error.message}`, ['error']);
            container.appendChild(errMsg);
        });
}

// Example usage (update 'https://api.example.com/items' and 'item-list-container' in your HTML):
// fetchAndRenderList('https://api.example.com/items', 'item-list-container');

