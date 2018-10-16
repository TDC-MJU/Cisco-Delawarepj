angular.module('customFilter',[])
.filter('custom', function() {
  return function(input, search) {
    if (!input) return input;
    if (!search) return input;
    console.log(input)
    console.log(search)
    var expected = ('' + search).toLowerCase();
    var result = {};
    angular.forEach(input, function(value, key) {
      var actual = ('' + value).toLowerCase();
      console.log(actual)
      console.log(value)
      if (actual.indexOf(expected) !== -1) {
        result[key] = value;
      }
    });
    return result;
  }
});