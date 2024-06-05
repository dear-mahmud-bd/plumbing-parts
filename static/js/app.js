
document.addEventListener("DOMContentLoaded", function() {
    var logoutLinks = document.querySelectorAll(".logout-link");
    logoutLinks.forEach(function(logoutLink) {
        logoutLink.addEventListener("click", function(event) {
            event.preventDefault();
            var confirmed = confirm("Are you sure you want to log out?");
            if (confirmed) {
                window.location.href = logoutLink.href;
            }
        });
    });
});  

