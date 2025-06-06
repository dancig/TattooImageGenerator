// Функция валидации текстового запроса
// Принимает строку текстового запроса
// Возвращает значение True, если строка содержит только слова на кириллице или латинице и цифры,
// Иначе возращает значение False
function validateText(text) {
	if (text.length == 0)
		return false;
    return /^(([А-Яа-я]+\s)||([A-Za-z]+\s)|([А-Яа-я]+$)|([A-Za-z]+$)|([0-9]+\s)|([0-9]+$))+$/.test(text)
}

const form = document.getElementById("form");
const textarea = document.getElementById("prompt");

// При отправке формы вызывается функция валидации текста формы
form.addEventListener("submit", function() {
    // Если текст запроса не прошел валидацию отправка формы отменяется
    // На экран выводится диалог о некорректном вводе
    if (!validateText(textarea.value)) {
        event.preventDefault();
        alert("Некорректный ввод");
    }
});