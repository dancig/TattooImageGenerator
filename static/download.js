// Функция сохранения сгенерированного изображения
// Возвращает значение True, если изображение успешно сохранено, иначе возвращает False
function downloadImage() {
    try {
        const link = document.createElement('a');
        link.href = 'static/images/image.png';      // Путь к сгенерированному изображению
        link.download = 'image.png';                // Имя сохраняемого файла
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

btn.addEventListener('click', downloadImage)        // При нажатии на кнопку "Сохранить" вызывается функция
                                                    // сохранения сгенерированного изображения изображения