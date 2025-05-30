/**
 * @jest-environment jsdom
 */

const downloadImage = require('./download');
describe("downloadImage", () => {
	
	// Файл по введенному пути существует
	// Должно возвращаться True
	test('File downloaded', () => {
		return expect(downloadImage('http://127.0.0.1:5000/static/images/image.png')).resolves.toBe(true);
	});
	
	// Файл по введенному пути не существует
	// Должно возвращаться False
	test('File not downloaded', () => {
		return expect(downloadImage('http://127.0.0.1:5000/static/images/images1231.png')).resolves.toBe(false);
	});
	
});