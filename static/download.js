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
    else	// Файл не существует
		alert("Ошибка при сохранении изображения.");
		return false;
}

const btn_img = document.getElementById("btn-dl-img");
const path_img = document.getElementById("img").src;
const btn_img_no_bg = document.getElementById("btn-dl-img-no-bg");
const path_img_no_bg = document.getElementById("img-no-bg").src;

btn_img.addEventListener('click', function() {  // При нажатии на кнопку "Сохранить" вызывается функция
    downloadImage(path_img);                    // сохранения сгенерированного изображения изображения
});

btn_img_no_bg.addEventListener('click', function() {    // Сохранение изображения без фона
    downloadImage(path_img_no_bg);
});