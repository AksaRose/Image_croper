document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('imageInput');
    const fileNameEl = document.getElementById('fileName');
    const cropBtn = document.getElementById('cropBtn');
    const shapeButtons = document.querySelectorAll('.shape-btn');
    const croppedImage = document.getElementById('croppedImage');
    const downloadBtn = document.getElementById('downloadBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');

    let selectedFile = null; // To store the selected file
    let selectedShape = null; // To store the selected shape

    imageInput.addEventListener('change', function(e) {
        selectedFile = e.target.files[0]; // Get the selected file
        if (selectedFile) {
            fileNameEl.textContent = selectedFile.name; // Display the file name
        }
        updateCropButton(); // Update crop button state
    });

    shapeButtons.forEach(button => {
        button.addEventListener('click', function() {
            shapeButtons.forEach(btn => btn.classList.remove('selected')); // Remove selection from all buttons
            this.classList.add('selected'); // Select the clicked button
            selectedShape = this.getAttribute('data-shape'); // Get the shape from the button
            updateCropButton(); // Update crop button state
        });
    });

    function updateCropButton() {
        cropBtn.disabled = !(selectedFile && selectedShape); // Enable/disable crop button based on selections
    }

    cropBtn.addEventListener('click', async function() {
        if (!selectedFile || !selectedShape) return;

        loadingIndicator.style.display = 'block'; // Show loading indicator

        const formData = new FormData();
        formData.append('file', selectedFile); // Append file to form data
        formData.append('shape', selectedShape); // Append shape to form data

        try {
            const response = await fetch('http://127.0.0.1:8000/crop', { // Send request to server
                method: 'POST',
                body: formData
            });

            if (!response.ok) throw new Error('Cropping failed.');

            const blob = await response.blob(); // Get cropped image as blob
            const croppedURL = URL.createObjectURL(blob); // Create object URL for cropped image
            croppedImage.src = croppedURL; // Set cropped image source
            croppedImage.style.display = 'block'; // Display cropped image
            downloadBtn.classList.remove('hidden'); // Show download button

            downloadBtn.onclick = () => { // Set up download functionality
                const a = document.createElement('a');
                a.href = croppedURL; 
                a.download = 'cropped_image.png'; 
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            };
        } catch (error) {
            alert(error.message); // Show error message if cropping fails
        } finally {
            loadingIndicator.style.display = 'none'; // Hide loading indicator
        }
    });
});