function squareNumber(num) {
    return num * num;
}

let result = squareNumber(5);
console.log("Square is:", result);


function checkOddEven(num) {
    if (num % 2 === 0) {
        return "Even";
    } else {
        return "Odd";
    }
}

console.log(checkOddEven(4)); // Even
console.log(checkOddEven(7)); // Odd