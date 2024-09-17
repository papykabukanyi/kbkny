document.addEventListener('DOMContentLoaded', () => {
    // Initialize Fullpage.js
    new fullpage('#fullpage', {
        autoScrolling: true,
        scrollHorizontally: false, // Disabled horizontal scrolling
        controlArrows: false,
        sectionsColor: ['#f2f2f2', '#4BBFC3', '#7BAABE', '#FF5F45'],
        navigation: true,
        onLeave: function (origin, destination, direction) {
            gsap.fromTo(
                destination.item,
                { opacity: 0 },
                { opacity: 1, duration: 1.5 }
            );

            // Update body background color to match section color
            const sectionColor = ['#f2f2f2', '#4BBFC3', '#7BAABE', '#FF5F45'];
            document.body.style.backgroundColor = sectionColor[destination.index];
        }
    });

    // Handle form submission
    const contactForm = document.getElementById('contactForm');
    
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent the default form submission

        const formData = new FormData(contactForm);
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        // Perform the fetch request
        fetch('/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(jsonData),
        })
        .then(response => {
            // Check if response is not okay (not in 200 range)
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.error); });
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('Message sent successfully!');
                contactForm.reset();  // Reset the form after successful submission
            } else {
                alert('Error sending message: ' + data.error);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while sending your message: ' + error.message);
        });
    });
});
