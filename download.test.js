/**
 * @jest-environment jsdom
 */

const downloadImage = require('./download');
describe("downloadImage", () => {
	
	test('File downloaded', () => {
		
		return expect(downloadImage('http://127.0.0.1:5000/static/images/image.png')).resolves.toBe(true);
	});
	
	test('File not downloaded', () => {
		return expect(downloadImage('http://127.0.0.1:5000/static/images/images1231.png')).resolves.toBe(false);
	});
	
});