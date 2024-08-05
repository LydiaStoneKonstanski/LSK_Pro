// When the user clicks on the button,
//toggle between hiding and showing the dropdown content
function menuFunction() {
    document.getElementById("read-more-qual").classList.toggle("show");
}
// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.btn-secondary')) {
        var dropdowns = document.getElementsByClassName("dropdown-content-two");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
// Function to perform the action on the target element
function performActionOnElement(targetId) {
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
        // Example action: toggle a class
        targetElement.classList.toggle('show');
    } else {
        console.error(`No element found with ID: ${targetId}`);
    }
}

// Add event listener to all buttons
document.querySelectorAll('.action-button').forEach(button => {
    button.addEventListener('click', function() {
        const targetId = this.getAttribute('data-target-id');
        performActionOnElement(targetId);
    });
});