#!/usr/bin/node
const newSquare = require('./5-square.js');

class Square extends newSquare {
	constructor (size) {
		super(size, size);
	}

	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.width; i++) {
			console.log(c.repeat(this.height));
		}
	}
}
module.exports = Square;
