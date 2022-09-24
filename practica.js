const numeros = [10, 20, 30, 40, 50];

const data = numeros.reduce((prev, curr) => {
  return prev + curr;
}, 0);
console.log(data);
