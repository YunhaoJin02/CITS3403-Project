document.addEventListener('DOMContentLoaded', function() {
    fetch('events.json')
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
            <li><a href="event_detail.html?id=${event.id}">View this event</a></li> <!-- Use event.id here -->
          </ul>
        </div>
        `;
    });
    
    
    container.innerHTML = htmlContent; // Insert the HTML into the container

    
    // Assuming we're only displaying the first event for simplicity
    const event = events[0];
    const eventHtml = `
        <h2>${event.title}</h2>
        <p>Date: ${event.date}</p>
        <p>Location: ${event.location}</p>
        <p>${event.description}</p>
        <!-- Commenting out the image since it's invalid -->
        <!-- <img src="${event.image}" alt="${event.title} Event" /> -->
    `;
    
    container.innerHTML = eventHtml; // Insert the HTML into the container

}
