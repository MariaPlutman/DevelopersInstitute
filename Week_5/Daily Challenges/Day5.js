// *
// * *
// * * *
// * * * *
// * * * * *

var i, j;
//outer loop
for (i = 1; i <= 5; i++) {
    //inner loop
    for (j = 1; j <= i; j++) {
        document.write('*');
    }
    document.write('<br/>');
}


//         *
//       * * *
//     * * * * *
//   * * * * * * *
// * * * * * * * * *

function pyramid(n) {
    for (var i = 1; i <= n; i++) {
        var myval = ' '.repeat(n - i);
        var myval1 = '*'.repeat(i * 2 - 1)
        console.log(myval + myval1 + myval);
    }
}
pyramid(5);