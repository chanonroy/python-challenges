/*
Given two strings a and b that may or may not be of the same length,
determine the minimum number of character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings.

https://www.hackerrank.com/challenges/ctci-making-anagrams
*/

function anagram_difference(a, b) {

    // Build counter array
    var count_array = [];
    for (var i = 0; i < 26; i++) {
      count_array[i] = 0;
    }

    // Count for first string
    for (var i in a) {
      var index = a[i].charCodeAt(0) - 'a'.charCodeAt(0);
      count_array[index] += 1;
    }

    // Count for second strings
    for (var i in b) {
      var index = b[i].charCodeAt(0) - 'a'.charCodeAt(0);
      count_array[index] -= 1;

    }

    // Get absolute values of changes
    var diff_count = 0;
    for (var i in count_array) {
      diff_count += Math.abs(count_array[i]);
    }

    console.log(diff_count);
    return diff_count;
}
