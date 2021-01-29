function minNumberInRotateArray(rotateArray) {
  // write code here'
  if (rotateArray.length == 0) return 0;

  let left = 0;
  let right = rotateArray.length - 1;
  let mid = 0;
  while (left < right) {
    if (rotateArray[left] < rotateArray[right]) return rotateArray[left];
    mid = left + (right - left) / 2;
    if (rotateArray[left] < rotateArray[mid]) {
      left = mid + 1;
    } else if (rotateArray[mid] < rotateArray[right]) {
      right = mid;
    } else {
    }
  }
  return rotateArray[mid];
}

console.log(minNumberInRotateArray([3, 4, 5, 1, 2]));
