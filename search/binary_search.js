var array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];

/**
* @param {Numbers[]} arr - sorted array of numbers
* @param {Number} value - value to be searched
*/
function binarySearch(arr, value) {

  console.log('Searching for ' + value);

  var min_index = 0;
  var max_index = arr.length - 1;
  var found = false;
  var found_index;

  while (min_index <= max_index && found !== true) {

    var middle_index = Math.floor((max_index + min_index) / 2);
    var number = arr[middle_index];

    console.log('Evaluating: ' + arr[middle_index] + ' ...');

    if (number == value) {
      found_index = middle_index;
      found = true;
    } else {
      // not found
      if (number < value) {
        // go right
        min_index = middle_index + 1;
      } else {
        // go left
        max_index = middle_index - 1;
      }
    }
  }

  return found ? 'Found ' + value + ' at index of ' + found_index : 'Not found';

}

console.log(binarySearch(array, 14));
