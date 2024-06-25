document.addEventListener('DOMContentLoaded', function() {
    const alvoLogos = document.querySelectorAll('.alvo-logo');

    alvoLogos.forEach(logo => {
        logo.closest('button').addEventListener('dblclick', function() {
            const containerId = this.getAttribute('data-container-id');
            fetchContainerProcess(containerId);
        });
    });

    function fetchContainerProcess(containerId) {
        fetch('/top/' + containerId)
            .then(response => response.json())
            .then(data => {
                displayContainerProcess(data);
            })
            .catch(error => console.error('Error fetching container process:', error));
    }

    function displayContainerProcess(data) {
        const containerTop = document.getElementById('container-top');
        let topHtml = '<table><thead><tr>';
        data.Titles.forEach(title => {
            topHtml += '<th>' + title + '</th>';
        });
        topHtml += '</tr></thead><tbody>';
        data.Processes.forEach(process => {
            topHtml += '<tr>';
            process.forEach(item => {
                topHtml += '<td>' + item + '</td>';
            });
            topHtml += '</tr>';
        });
        topHtml += '</tbody></table>';
        containerTop.innerHTML = topHtml;
        containerTop.style.display = 'block'; // Make the container process section visible
    }
});
