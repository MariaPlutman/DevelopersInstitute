function verbing(word) {
  if (word.length < 3) return word;
  if (word.slice(-3) == 'ing') {
    return word + 'ly';
  } else {
    return word + 'ing';
  }
}