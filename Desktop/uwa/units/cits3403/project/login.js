// Add event listener to the window object to ensure the DOM is fully loaded
window.addEventListener('DOMContentLoaded', (event) => {
    // Function to handle staff login
    function handleStaffLogin(event) {
        event.preventDefault(); // Prevent the default form submission

        var username = document.getElementById('staff-username').value;
        var password = document.getElementById('staff-pwd').value;

        // Fake credentials for staff
        var fakeUsername = 'staff1';
        var fakePassword = 'staff1';

        // Simple check for the fake credentials (replace with AJAX in the future)
        if(username === fakeUsername && password === fakePassword) {
            // Redirect to a logged-in page or change the interface
            window.location.href = 'staff_area.html'; // Redirect to staff area
        } else {
            // Show an error message
            alert('Incorrect username or password. Please try again.');
        }
    }

    // Future AJAX call for real authentication (commented out)
    /*
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/login-endpoint', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
        if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Handle successful login
        } else {
            // Handle error
        }
    };
    xhr.send('username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password));
    */

    // Attach the event listener to the staff login form
    var staffLoginForm = document.getElementById('staff-login');
    if (staffLoginForm) {
        staffLoginForm.addEventListener('submit', handleStaffLogin);
    }
});
