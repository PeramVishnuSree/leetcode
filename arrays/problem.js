// given two words, return true if only two letters are swapped adn false in all other cases

function iscorrect(word, swapped) {
  if (word.length != swapped.length) return false;
  let arr = [];
  for (let i = 0; i < word.length; i++) {
    if (word[i] === swapped[i]) continue;
    arr.push([word[i], swapped[i]]);
  }
  if (arr.length != 2) return false;
  if (arr[0][0] === arr[1][1] && arr[0][1] === arr[1][0]) return true;
  return false;
}
