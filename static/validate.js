function validateText(text) {
    return /([А-Яа-я0-9]+\s?)+|([A-Za-z0-9]+\s?)+/.test(text)
}

const form = document.getElementById("form");
const textarea = document.getElementById("prompt");

form.addEventListener("submit", function(event) {
    if (!validateText(textarea.value)) {
        event.preventDefault();
        alert("Некорректный ввод");
    }
});