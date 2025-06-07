// Асинхронная функция отправки запроса на удаление заднего фона сгенерированного изображения
// Принимает путь до сгенерированного изображения, пороговое значение, булевые значения эрозии и дилатации изображения
// Отправляет JSON запрос с входными данными
// Если код ответа = 200, то отображает изображение на странице
// Иначе отображает сообщение об ошибке
async function remove_background(img_path, threshold_value, erode, dilate) {
    let data = {
        path: img_path,
        threshold: threshold_value,
        erode: erode,
        dilate: dilate
    };

    let response = await fetch('/', {
        method: 'POST',
        cache: 'reload',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data)
    });

    if(response.ok){
        let result = await response.json();
        await fetch(result.image, {cache: 'reload'})
        img_no_bg.src = result.image;
        btn_download_no_bg.disabled = false;
    }
    else {
        alert('Ошибка удаления фона');
    }
}

const path_src_img = document.getElementById("img").src;
const img_no_bg = document.getElementById("img-no-bg");
const threshold = document.getElementById("threshold");
const erosion = document.getElementById("erosion");
const dilation = document.getElementById("dilation");
const threshold_label = document.getElementById("threshold-label");
const btn_remove = document.getElementById("btn-rm-bg");
const btn_download_no_bg = document.getElementById("btn-dl-img-no-bg");

// При изменении ползунка изменяется подпись со значением
threshold.addEventListener('input', function() {
    threshold_label.innerText = `Порог = ${threshold.value}`;
});

// При нажатии на кнопку 'Удалить фон' отправляется запрос на удаление фона
btn_remove.addEventListener('click', function() {
    remove_background(path_src_img, threshold.value, erosion.checked, dilation.checked)
});