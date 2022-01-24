const queryString = location.search;
console.log(queryString);

const urlParams = new URLSearchParams(queryString);
console.log(urlParams);

const candidato = urlParams.get("candidato");

console.log(candidato);