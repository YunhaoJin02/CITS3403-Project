// Function that will be called to display the event details
function displayEventDetails(event) {
    // Assuming you have placeholders for these details in your event_detail.html
    document.getElementById('event-title').textContent = event.title;
    document.getElementById('event-date').textContent = `Date: ${event.date}`;
    document.getElementById('event-location').textContent = `Location: ${event.location}`;
    document.getElementById('event-description').textContent = event.description[0].subheader;
    document.getElementById('img1').src = event.img1;
    document.getElementById('img2').src = event.img2;
    document.getElementById('img3').src = event.img3;
    document.getElementById('img4').src = event.img4;

    document.getElementById('event-price').src = `Price: ${event.price}`;

    const priceInfo = event.price === 0 ? 'Free' : `$${event.price}`;
    document.getElementById('event-price').textContent = `Ticket fee: ${priceInfo}`;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    // Parse the URL parameter to get the event index
    const params = new URLSearchParams(window.location.search);
    const eventID = parseInt(params.get('id'), 10);
  
    // Fetch the events data
    fetch('events.json')
      .then(response => response.json())
      .then(data => {
        // Access the events array inside the data object
        const events = data.events;
        // Use the eventIndex to access the specific event object
        const event = events.find(e => e.id === eventID); // No need to use find() because we have the index
        if (event) {
          displayEventDetails(event);
        } else {
          console.error('Event not found');
        }
      })
      .catch(error => {
        console.error('Error loading event details:', error);
      });
  });
  
  