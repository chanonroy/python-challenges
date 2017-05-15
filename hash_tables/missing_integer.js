/*
Write a function that, given a non-empty zero-indexed array A of N integers,
returns the MINIMAL POSITIVE integer (greater than 0) that does not occur in A.

Example:
[1, 3, 6, 4, 1, 2] is missing 5

Assumptions:
1) N is an integer within the range [1..100,000];
2) Each element of the array is an integer within the range [−2,147,483,648..2,147,483,647].

TODO: Needs factoring, fails a lot of test cases
*/

function missing_integer(array) {

  var length = array.length;
  var count_map = {};

  // build map
  for (var i = 0; i < length; i++) {
    if (count_map[array[i]]) {
      count_map[array[i]] += 1;
    } else {
      count_map[array[i]] = 1;
    }
  }

  // evaluate array
  for (var i = 0; i < length; i++) {

    var number = array[i] - 1;

    if (count_map[number] == undefined && number >= 1) {
      return number >= 1 ? number : -1;
    } else {
      continue
    }
  }

  return -1

}
