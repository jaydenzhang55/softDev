//Team Margie - Margie Cao, Jayden Zhang
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

let fact = function(n) {
    if (n == 1) return 1;
    else return n * fact(n-1);
}

//TEST CALLS
fact(1) // 1
fact(5) // 120
fact(10) // 3628800

//-----------------------------------------------------------------


//fib:

function fib(n){
  if (n == 1) return 1;
  else if (n == 2) return 1;
    else return fib(n - 1) + fib(n - 2); 
}

//TEST CALLS

fib(1) // 1
fib(2) // 1
fib(3) // 2
fib(5) // 5
fib(10) // 55

//=================================================================

