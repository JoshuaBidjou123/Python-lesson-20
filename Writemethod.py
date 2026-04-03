var fs = require('fs');

//create a file named mynewfile3.txt:
fs.writeFile('mytextfile.txt', 'I change the content', function (err) {
    if (err) throw err;
    console.log('Content change d!');
});

var fs = require('fs');

//Delete the file mynewfile2.txt:
fs.unlink('newfile.txt', function (err) {
    if (err) throw err;
    console.log('File deleted!');
});

var fs = require('fs');

//Rename the file "mynewfile1.txt" into "myrenamedfile.txt":
fs.rename('file.txt', 'myrenamedfile1.txt', function (err) {
    if (err) throw err;
    console.log('File Renamed!');
}); 