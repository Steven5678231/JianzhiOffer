const inStack = [];
const outStack = [];

function push(node) {
  inStack.push(node);
  // write code here
}
function pop() {
  if (outStack.length) {
    return outStack.pop();
  } else {
    while (inStack.length) {
      outStack.push(inStack.pop());
    }
    return outStack.pop();
  }
  // write code here
}

push(1);
push(2);
console.log(pop());
