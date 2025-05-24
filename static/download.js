// Асинхронная функция сохранения сгенерированного изображения
// Сохраняет сгенерированное изображение на устройство пользователя
// Принимает путь до изображения
// Возвращает true, если файл существует и сохранен
// Если файл не существует, то возвращает false
async function downloadImage(img_path) {
	let response = await fetch(img_path);	// Проверка существования файла
    if (response.ok) {
		// Файл существует		
		const link = document.createElement('a');
		link.href = img_path;         // Путь к сгенерированному изображению
		link.download = img_path;     // Имя сохраняемого файла
		document.body.appendChild(link);
		link.click();
		document.body.removeChild(link);
		return true;
    }
    else
		return false;
}

const btn = document.getElementById("btn-dl");
const path = document.getElementById("img").src;

btn.addEventListener('click', function() {  // При нажатии на кнопку "Сохранить" вызывается функция
    downloadImage(path)                     // сохранения сгенерированного изображения изображения
});