function sortToCloseBlocksTogether() {
    data = loadFile('data', 'blaze');

    console.log('Data:')
    console.log(data);


    flatternedData = [].concat(...Object.values(data)); // Removes dict keys and the concatinates the arrays to make one big array :) 

    console.log('Flatterned:')
    console.log(flatternedData);

    // flatternedData.sort(function(a, b) {
    // return a[0][2] - b[0][2];
    // });

    flatternedData.sort(function(a, b) {
        // Compare all three coordinates
        for (let i = 0; i < 3; i++) {
            if (a[0][i] !== b[0][i]) {
                return a[0][i] - b[0][i];
            }
        }
        // If all coordinates are equal, compare the block type
        return a[1].localeCompare(b[1]);
    });

    console.log('Sorted:')
    console.log(flatternedData);

    const fs = require('fs');

    fs.writeFile('Blaze-Sorted.txt', '', (err) => {if (err) throw err});

    for (var i in flatternedData) {
        i = flatternedData[i]
        console.log(i);
        fs.appendFile('Blaze-Sorted.txt', i + '\n', (err) => {
            if (err) console.log('Couldnt append');//throw err;
        })
    }
}


function loadFile(filepath='data', filename='test') {
    try {
        var data = require(`./${filepath}/${filename}.json`);
        return data;
    } catch (error) {
        console.log(error);
        return;
    }
}


sortToCloseBlocksTogether();