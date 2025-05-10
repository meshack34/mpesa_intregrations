// Function to show the popup form
function openForm() {
    document.getElementById("popup-overlay").classList.add("active"); // Show overlay
    document.getElementById("popup-form").classList.add("active"); // Show form
}

// Function to close the popup form
function closeForm() {
    document.getElementById("popup-overlay").classList.remove("active"); // Hide overlay
    document.getElementById("popup-form").classList.remove("active"); // Hide form
}

// Ensure the close button works
document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".close-btn").addEventListener("click", closeForm);

    // Allow clicking outside the form to close it
    document.getElementById("popup-overlay").addEventListener("click", closeForm);
});
