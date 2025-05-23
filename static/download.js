// Функция сохранения сгенерированного изображения
// Сохраняет сгенерированное изображение на устройство пользователя
// При возвникновении ошибки выводит на экран сообщении об ошибке
function downloadImage() {
    const path = document.getElementById("img").src;
    fetch(path).then(response => {  // Проверка существования файла
        if (response.ok) {          // Файл существует
            const link = document.createElement('a');
            link.href = path;         // Путь к сгенерированному изображению
            link.download = path;     // Имя сохраняемого файла
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
        else
            alert("Произошла ошибка при сохранении файла."); // Файл не существует
    })
}

const btn = document.getElementById("btn-dl");

btn.addEventListener('click', downloadImage)        // При нажатии на кнопку "Сохранить" вызывается функция
                                                    // сохранения сгенерированного изображения изображения