let str = prompt("Give me several words:");
function freq(s) {
    console.log(s);
    let i, j;
    let a = new Array();
    for (j = 0; j < s.length; j++) {
        for (i = 0; i < a.length; i++) {
            if (a[i][0] == s[j]) {
                a[i][1]++;
                break;
            }
        }
        if (i == a.length) {
            a[i] = [s[j], 1];
        }
    }
    return a;
}
let all_words = str.split(' ');
let all_freq = all_words.map(freq);
console.log(all_freq);
let max_freq = 0;
let max_word;
for (let i = 0; i < all_freq.length; i++) {
    for (j = 0; j < all_freq[i].length; j++) {
        if (all_freq[i][j][1] > max_freq) {
            max_freq = all_freq[i][j][1];
            max_word = i;
        }
    }
}
console.log(all_words[max_word]);