#!/usr/bin/node
const argsLength = process.argv.length;
if (process.argv.length === 2) {
	console.log('No argument');
} else if (argsLength === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
