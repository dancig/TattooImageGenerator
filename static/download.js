function downloadImage() {
    try {
        const link = document.createElement('a');
        link.href = 'static/images/image.png';
        link.download = 'image.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        console.log("Image downloaded");
        return true;
    }
    catch(error) {
        console.log(error);
        return false;
    }
}

const btn = document.getElementById("btn-dl");
btn.addEventListener('click', downloadImage)