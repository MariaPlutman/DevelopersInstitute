function notBad(sentence) {
  var notIndex = sentence.indexOf('not');
  var badIndex = sentence.indexOf('bad');
  if (notIndex == -1 || badIndex == -1 || badIndex < notIndex) return sentence;
  return sentence.slice(0, notIndex) + 'good' + sentence.slice(badIndex + 3);
}