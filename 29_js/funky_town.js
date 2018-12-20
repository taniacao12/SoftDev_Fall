// Team Apricot (Mohtasim Howlader and Tania Cao Su)
// SoftDev1 pd8
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-20

var fibonacci = function(n) {
    if (n == 0)
    return 0;
    if (n == 1)
    return 1;
    else
    return fibonacci(n-1) + fibonacci(n-2);
};

var gcd = function(a,b) {
    if (a == 0) {
        return b;
    }
    if (b == 0) {
        return a;
    }
    return gcd(b,a%b);
};


var students = ["mohtasim", "soojin", "bob", "sam", "emily"];

var randomStudent = function() {
    randInd = Math.random() * students.length;
    return students[Math.floor(randInd)];

}

// var test = function() {
//     console.log(5);
// }
//
// var dasbut = document.getElementById("a");
// dasbut.addEventListener("click", test);

//Fibonacci Button
var fibber = document.getElementById("fibButton");
var fibstuf = document.getElementById("fibRes");

fibber.addEventListener("click", function(){
    ans = fibonacci(10);
    fibstuf.innerHTML = ans;
    console.log("fibonacci(10) = " + fibstuf.innerHTML);
});

//GCD button
var gcder = document.getElementById("gcdButton");
var gcdstuf = document.getElementById("gcdRes");

gcder.addEventListener("click", function(){
    ans = gcd(27,6);
    gcdstuf.innerHTML = ans;
    console.log("gcd(27,6) = " + gcdstuf.innerHTML);
});

//Random student button
var raner = document.getElementById("ranButton");
var ranstuf = document.getElementById("ranRes");

raner.addEventListener("click", function(){
    ans = randomStudent();
    ranstuf.innerHTML = ans;
    console.log("randomStudent() = " + ranstuf.innerHTML);
});
