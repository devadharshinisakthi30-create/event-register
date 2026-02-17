// Form validation and enhancement
document.addEventListener('DOMContentLoaded', function() {
    // Set minimum date to today for event date selection
    const dateInput = document.getElementById('date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }

    // Form submission validation
    const registrationForm = document.querySelector('.registration-form');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function(e) {
            // Check if at least one event is selected
            const eventCheckboxes = document.querySelectorAll('input[name="events"]:checked');
            
            if (eventCheckboxes.length === 0) {
                e.preventDefault();
                alert('⚠️ Please select at least one event to register!');
                return false;
            }
            
            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '⏳ Processing...';
                submitBtn.disabled = true;
            }
        });
    }

    // Phone number validation
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            // Remove non-numeric characters
            this.value = this.value.replace(/[^0-9]/g, '');
            
            // Limit to 10 digits
            if (this.value.length > 10) {
                this.value = this.value.slice(0, 10);
            }
        });
    }

    // Event checkbox animation
    const eventCheckboxes = document.querySelectorAll('.event-checkbox input[type="checkbox"]');
    eventCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const label = this.nextElementSibling;
            if (this.checked) {
                label.style.animation = 'pulse 0.3s ease';
            }
            setTimeout(() => {
                label.style.animation = '';
            }, 300);
        });
    });

    // Table search functionality (if needed in admin dashboard)
    const searchInput = document.getElementById('tableSearch');
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const filter = this.value.toUpperCase();
            const table = document.querySelector('.data-table');
            const rows = table.getElementsByTagName('tr');

            for (let i = 1; i < rows.length; i++) {
                let row = rows[i];
                let textContent = row.textContent || row.innerText;
                
                if (textContent.toUpperCase().indexOf(filter) > -1) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            }
        });
    }

    // Add animation to stat cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });

    // Success message auto-scroll
    if (document.querySelector('.success-card')) {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
});

// Add CSS animation classes
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes fade-in {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fade-in 0.5s ease forwards;
    }
`;
document.head.appendChild(style);
