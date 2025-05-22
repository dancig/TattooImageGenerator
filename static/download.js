// Функция сохранения сгенерированного изображения
// Сохраняет сгенерированное изображение на устройство пользователя
function downloadImage() {
    const link = document.createElement('a');
    link.href = document.getElementById("img").src;         // Путь к сгенерированному изображению
    link.download = document.getElementById("img").src;     // Имя сохраняемого файла
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

const btn = document.getElementById("btn-dl");

btn.addEventListener('click', downloadImage)        // При нажатии на кнопку "Сохранить" вызывается функция
                                                    // сохранения сгенерированного изображения изображения