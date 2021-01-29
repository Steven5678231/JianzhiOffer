function jumpFloor(number) {
  if (number == 1) return 1;
  if (number == 2) return 2;
  if (number == 3) return 3;
  var myArray = new Array();
  myArray[1] = 1;
  myArray[2] = 2;
  myArray[3] = 3;

  for (let i = 4; i < number + 1; i++) {
    myArray[i] = myArray[i - 1] + myArray[i - 2];
  }
  return myArray[number];
  // write code here
}
console.log(jumpFloor(4));
