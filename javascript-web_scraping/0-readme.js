#!/usr/bin/node
let fs = require('fs');
fs.readFile(filename, 'utf-8', function (err, data) {
	if (err) throw err;
	console.log(data);
}
