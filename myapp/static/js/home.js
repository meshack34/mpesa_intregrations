<script>
document.addEventListener("DOMContentLoaded", function() {
    // Enable hover dropdown only on larger screens
    if (window.innerWidth > 992) {
        document.querySelectorAll('.navbar .dropdown').forEach(function(dropdown) {
            dropdown.addEventListener('mouseenter', function() {
                let menu = this.querySelector('.dropdown-menu');
                menu.classList.add('show');
            });

            dropdown.addEventListener('mouseleave', function() {
                let menu = this.querySelector('.dropdown-menu');
                menu.classList.remove('show');
            });
        });
    }
});
</script>
