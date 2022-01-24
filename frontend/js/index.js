const txtCedula = document.getElementById("dni");
const btnConsulta = document.getElementById("button");

const URI = "http://127.0.0.1:5500/frontend/html/";

const getVoter = async dni => {
    const URL = `http://localhost:3000/votantes/${dni}/`;
    const config = { method: "GET", headers: { Accept: "application/json", ContentType: "application/json" } };
    const result = { data: null, success: false };
    try {
        const response = await fetch(URL, config);
        if (!response.ok) return result;
        const json = await response.json();
        return json;
    } catch (error) {
        console.error(error);
        return result;
    }
}

btnConsulta.addEventListener("click", async () => {
    const dni = txtCedula.value.trim().toLowerCase();
    console.log(dni);
    const { data, success } = await getVoter(dni);
    console.table(data, success);
    alert(JSON.stringify(data));
    if (success) location.href = URI.concat("candidatos.html?candidato=1");
});