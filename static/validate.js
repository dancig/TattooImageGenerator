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

form.addEventListener("submit", function(event) {   // При отправке формы вызывается функция валидации текста формы
    if (!validateText(textarea.value)) {
        event.preventDefault();                     // Если текст запроса не прошел валидацию отправка формы отменяется
        alert("Некорректный ввод");                 // На экран выводится диалог о некорректном вводе
    }
});