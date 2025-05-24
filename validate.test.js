const validateText = require('./validate');

describe('validateText', () => {
	//Test 1
	test('should return true for string "hello"', () => {
		expect(validateText('hello')).toBe(true);
	});
	//Test 2
	test('should return true for string "hello Hello"', () => {
		expect(validateText('hello Hello')).toBe(true);
	});
	//Test 3
	test('should return true for string "Hello привет 1231"', () => {
		expect(validateText('Hello привет 1231')).toBe(true);
	});
	//Test 4
	test('should return true for string "привет Привет"', () => {
		expect(validateText('привет Привет')).toBe(true);
	});
	//Test 5
	test('should return true for string "Привет 123"', () => {
		expect(validateText('Привет 123')).toBe(true);
	});
	//Test 6
	test('should return true for string "привет"', () => {
		expect(validateText('привет')).toBe(true);
	});
	//Test 7
	test('should return true for string "1231"', () => {
		expect(validateText('1231')).toBe(true);
	});
	//Test 8
	test('should return true for string ""', () => {
		expect(validateText('')).toBe(false);
	});
	//Test 9
	test('should return true for string "hello"', () => {
		expect(validateText('приветhello')).toBe(false);
	});
	//Test 10
	test('should return true for string "hello"', () => {
		expect(validateText('helloпривет')).toBe(false);
	});
	//Test 11
	test('should return true for string "hello"', () => {
		expect(validateText('привет123')).toBe(false);
	});
	//Test 12
	test('should return true for string "hello"', () => {
		expect(validateText('hello123')).toBe(false);
	});
	//Test 13
		test('should return true for string "hello"', () => {
		expect(validateText('123привет')).toBe(false);
	});
	//Test 14
	test('should return true for string "hello"', () => {
		expect(validateText('123hello')).toBe(false);
	});
	//Test 15
	test('should return true for string "hello"', () => {
		expect(validateText('@%#@!! hello')).toBe(false);
	});
});