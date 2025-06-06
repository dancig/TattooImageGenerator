// Асинхронная функция сохранения сгенерированного изображения
// Сохраняет сгенерированное изображение на устройство пользователя
// Принимает путь до изображения
// Возвращает true, если файл существует и сохранен
// Если файл не существует, то возвращает false
async function downloadImage(img_path) {
	// Проверка существования файла
	let response = await fetch(img_path);
    if (response.ok) {
		// Файл существует		
		const link = document.createElement('a');
		// Путь к сгенерированному изображению
		link.href = img_path;
		// Имя сохраняемого файла
		link.download = img_path;
		document.body.appendChild(link);
		link.click();
		document.body.removeChild(link);
		return true;
    }
    else
        // Файл не существует
		alert("Ошибка при сохранении изображения.");
		return false;
}

const btn_img = document.getElementById("btn-dl-img");
const path_img = document.getElementById("img");
const btn_img_no_bg = document.getElementById("btn-dl-img-no-bg");
const path_img_no_bg = document.getElementById("img-no-bg");

// При нажатии на кнопку "Сохранить" вызывается функция
// сохранения сгенерированного изображения изображения
btn_img.addEventListener('click', function() {
    downloadImage(path_img.src);
});

// Сохранение изображения без фона
btn_img_no_bg.addEventListener('click', function() {
    downloadImage(path_img_no_bg.src);
});