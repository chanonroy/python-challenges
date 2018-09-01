function one() {
    // Problematic implementation
    for (var i = 0; i < 5; i++) {
        setTimeout(function() {
            console.log(i);
        }, 1000);
    }
    // returns '5, 5, 5, 5, 5'
}

function two() {
    // Problematic implementation
    for (var i = 0; i < 5; i++) {
        setTimeout(function() {
            console.log(i);
        }, 0);
    }
    // returns '5, 5, 5, 5, 5'
}

function three() {
    // Let declaration
    for (let i = 0; i < 5; i++) {
        setTimeout(function() {
            console.log(i);
        }, 1000);
    }
    // returns '0, 1, 2, 4, 5'
}

function four() {
    // Wrapped inside an IEFE
    for (var i = 0; i < 5; i++) {
        (function(i) {
            setTimeout(function() { console.log(i); }, 1000);
        })(i);
    }
    // returns '0, 1, 2, 4, 5'
}

one();
