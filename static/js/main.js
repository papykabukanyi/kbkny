document.addEventListener('DOMContentLoaded', () => {
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

    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(contactForm);
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        fetch('/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(jsonData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Message sent successfully!');
                contactForm.reset();
            } else {
                alert('Error sending message.');
            }
        });
    });
});
