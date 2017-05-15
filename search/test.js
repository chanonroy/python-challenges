var assert = require('assert');
var expect = require("chai").expect;
var module = require("./binary_search");

describe("Binary Search", function() {

    it("Finds the right number in a generic list", function() {
      var array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
      var test = module.binarySearch(array, 5, false);
      expect(test).to.equal(true);
    });

    it("Finds the right number when there is one number", function() {
      var array = [1];
      var test = module.binarySearch(array, 1, false);
      expect(test).to.equal(true);
    });

});
