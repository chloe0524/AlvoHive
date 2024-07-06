document.addEventListener("DOMContentLoaded", function() {
    const editedRows = new Set();

    const grid = new gridjs.Grid({
        columns: [
            { id: 'id', name: 'ID' },
            { id: 'name', name: 'Name', editable: true },
            { id: 'value', name: 'Value', attributes:{ "contenteditable" : "true"}}
        ],
        server: {
            url: '/test_items/items',
            then: data => data.map(item => [item.id, item.name, item.value])
        },
        pagination: true,
        search: true,
        sort: true,
        resizable: true,
        className: {
            td: 'gridjs-td',
            th: 'gridjs-th'
        },
        style: {
            table: {
                'width': '100%',
                'border': '1px solid #ccc'
            },
            th: {
                'background-color': '#f5f5f5',
                'border': '1px solid #ccc',
                'padding': '5px'
            },
            td: {
                'border': '1px solid #ccc',
                'padding': '5px'
            }
        }
    }).render(document.getElementById("grid"));

    document.getElementById("add-item").addEventListener("click", function() {
        const name = document.getElementById("name").value;
        const value = document.getElementById("value").value;

        fetch('/test_items/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, value })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                grid.updateConfig({
                    server: {
                        url: '/items'
                    }
                }).forceRender();
            }
        });
    });

    document.addEventListener('blur', function(e) {
        if (e.target.classList.contains('gridjs-input')) {
            const row = e.target.closest('.gridjs-tr');
            const id = row.querySelector('.gridjs-td:first-child').innerText;
            const columnName = e.target.closest('.gridjs-td').dataset.column;
            const newValue = e.target.value;

            const rowData = Array.from(row.querySelectorAll('.gridjs-td')).map(td => td.innerText);
            editedRows.add(rowData);

            rowData[columnName === 'name' ? 1 : 2] = newValue; // Update name or value in rowData
        }
    }, true);

    document.getElementById("commit-changes").addEventListener("click", function() {
        editedRows.forEach(rowData => {
            const payload = {
                id: rowData[0],
                name: rowData[1],
                value: rowData[2]
            };

            fetch('/test_items/update', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    grid.updateConfig({
                        server: {
                            url: '/items'
                        }
                    }).forceRender();
                }
            });
        });

        editedRows.clear(); // Clear the set after committing changes
    });

    document.getElementById("rollback-changes").addEventListener("click", function() {
        fetch('/test_items/rollback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                grid.updateConfig({
                    server: {
                        url: '/items'
                    }
                }).forceRender();
            }
        });

        editedRows.clear(); // Clear the set after rolling back changes
    });
});
