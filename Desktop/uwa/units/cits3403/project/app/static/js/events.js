document.addEventListener('DOMContentLoaded', function() {
    fetch('static/data/events.json')
        .then(response => response.json()) // Parse JSON response
        .then(data => {
            displayEvents(data.events); // Function to handle the display of events
        })
        .catch(error => console.error('Unable to get events:', error));
});

function displayEvents(events) {
    const container = document.getElementById('latest-event'); // Updated to target the latest-event ID

    let htmlContent = '';
    events.forEach((event) => {
        htmlContent += `
        <div class="event">
          <h3>${event.title}</h3>
          <p>Date: ${event.date}</p>
          <p>Location: ${event.location}</p>
          <ul>
            <li><a href="${baseEventDetailUrl}?id=${event.id}">View this event</a></li> <!-- Dynamically create the link -->
          </ul>
        </div>
        `;
    });
    
    
    container.innerHTML = htmlContent; // Insert the HTML into the container
}
