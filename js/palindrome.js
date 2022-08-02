// given a number, return true of it is a palindrome or false otherwise.

var isPalindrome = function (x) {
  if (x < 0) return false;
  let y = String(x);
  let i = 0;
  let j = y.length - 1;

  while (j > i) {
    if (y[i] != y[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
};
