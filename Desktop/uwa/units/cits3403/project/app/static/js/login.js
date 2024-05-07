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

    // Function to handle sign-up link click
    function handleSignUp(event) {
        event.preventDefault(); // Prevent the default link behavior
        window.location.href = 'sign_up.html'; // Redirect to sign-up page
    }

    // Attach the event listener to the staff login form
    var staffLoginForm = document.getElementById('staff-login');
    if (staffLoginForm) {
        staffLoginForm.addEventListener('submit', handleStaffLogin);
    }

    // Attach the event listener to the sign-up link
    var signUpLink = document.querySelector('.login-links a[href="sign_up.html"]');
    if (signUpLink) {
        signUpLink.addEventListener('click', handleSignUp);
    }
});
