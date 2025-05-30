const validateText = require('./validate');

describe('validateText', () => {
	
	// Проверяется строка 'hello'
	// Должно возвращаться True
	test('should return true for string "hello"', () => {
		expect(validateText('hello')).toBe(true);
	});
	
	// Проверяется строка 'hello Hello'
	// Должно возвращаться True
	test('should return true for string "hello Hello"', () => {
		expect(validateText('hello Hello')).toBe(true);
	});
	
	// Проверяется строка 'Hello привет 1231'
	// Должно возвращаться True
	test('should return true for string "Hello привет 1231"', () => {
		expect(validateText('Hello привет 1231')).toBe(true);
	});
	
	// Проверяется строка 'привет Привет'
	// Должно возвращаться True
	test('should return true for string "привет Привет"', () => {
		expect(validateText('привет Привет')).toBe(true);
	});
	
	// Проверяется строка 'Привет 123'
	// Должно возвращаться True
	test('should return true for string "Привет 123"', () => {
		expect(validateText('Привет 123')).toBe(true);
	});
	
	// Проверяется строка 'привет'
	// Должно возвращаться True
	test('should return true for string "привет"', () => {
		expect(validateText('привет')).toBe(true);
	});
	
	// Проверяется строка '1231'
	// Должно возвращаться True
	test('should return true for string "1231"', () => {
		expect(validateText('1231')).toBe(true);
	});
	
	// Проверяется строка ''
	// Должно возвращаться False
	test('should return false for string ""', () => {
		expect(validateText('')).toBe(false);
	});
	
	// Проверяется строка 'приветhello'
	// Должно возвращаться False
	test('should return false for string "приветhello"', () => {
		expect(validateText('приветhello')).toBe(false);
	});
	
	// Проверяется строка 'helloпривет'
	// Должно возвращаться False
	test('should return false for string "helloпривет"', () => {
		expect(validateText('helloпривет')).toBe(false);
	});
	
	// Проверяется строка 'привет123'
	// Должно возвращаться False
	test('should return false for string "привет123"', () => {
		expect(validateText('привет123')).toBe(false);
	});
	
	// Проверяется строка 'hello123'
	// Должно возвращаться False
	test('should return false for string "hello123"', () => {
		expect(validateText('hello123')).toBe(false);
	});
	
	// Проверяется строка '123привет'
	// Должно возвращаться False
		test('should return false for string "123привет"', () => {
		expect(validateText('123привет')).toBe(false);
	});
	
	// Проверяется строка '123hello'
	// Должно возвращаться False
	test('should return false for string "123hello"', () => {
		expect(validateText('123hello')).toBe(false);
	});
	
	// Проверяется строка '@%#@!! hello'
	// Должно возвращаться False
	test('should return false for string "@%#@!! hello"', () => {
		expect(validateText('@%#@!! hello')).toBe(false);
	});
});