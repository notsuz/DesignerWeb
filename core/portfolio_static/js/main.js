function redirectToGmail(event) {
        // Prevent the page from refreshing on form submit
        event.preventDefault();

        // 1. Collect what the viewer typed into the fields
        const viewerEmail = document.getElementById('viewerEmail').value;
        const messageBody = document.getElementById('viewerMessage').value;

        // 2. Set your configuration parameters
        const yourEmail = "madebysajit@gmail.com"; 
        const subject = encodeURIComponent("Portfolio Inquiry from " + viewerEmail);
        
        // Construct a clean, readable email body template
        const formattedBody = encodeURIComponent(
            "Hello Sujal,\n\n" + 
            messageBody + 
            "\n\n---\nSent via portfolio by: " + viewerEmail
        );

        // 3. Generate the direct Gmail web compose URL
        const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${yourEmail}&su=${subject}&body=${formattedBody}`;

        // 4. Open Gmail in a new browser tab instantly
        window.open(gmailUrl, '_blank');
    }