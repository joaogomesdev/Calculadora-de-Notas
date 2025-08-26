// Remover loading após 1 segundo
function esconderLoading() {
  const loading = document.getElementById("loading");
  if (loading) {
    loading.style.opacity = "0";
    setTimeout(() => { loading.style.display = "none"; }, 500);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  setTimeout(esconderLoading, 1000); // 1 segundo de loading
});

// Gerar campos de notas
function gerarCampos() {
  let bimestre = document.getElementById("bimestre").value;
  let campos = document.getElementById("camposNotas");
  campos.innerHTML = "";

  for (let i = 1; i <= bimestre; i++) {
    campos.innerHTML += `<h3>${i}º Bimestre</h3>`;
    campos.innerHTML += `<input type="text" id="nota${i}a" placeholder="Nota 1 do ${i}º" />`;
    campos.innerHTML += `<input type="text" id="nota${i}b" placeholder="Nota 2 do ${i}º" /><br><br>`;
  }
}

document.getElementById("bimestre").addEventListener("change", gerarCampos);
gerarCampos();

// Calcular médias
document.getElementById("btnCalcular").addEventListener("click", () => {
  let bimestre = parseInt(document.getElementById("bimestre").value);
  let resultado = document.getElementById("resultado");
  resultado.innerHTML = "";

  let medias = [];
  for (let i = 1; i <= bimestre; i++) {
    let n1 = parseFloat(document.getElementById(`nota${i}a`).value.replace(",", ".")) || 0;
    let n2 = parseFloat(document.getElementById(`nota${i}b`).value.replace(",", ".")) || 0;
    let media = (n1 + n2)/2;
    medias.push(media);

    let box = document.createElement("div");
    box.className = "result-box show";
    if (media >= 7) box.classList.add("success");
    else box.classList.add("warning");

    box.innerHTML = `<p>Média do ${i}º bimestre: <b>${media.toFixed(2)}</b></p>`;
    if (media < 7) box.innerHTML += `<p>⚠️ Você precisa de ${(7 - media).toFixed(2)} pontos para atingir a média.</p>`;
    else box.innerHTML += `<p>✅ Você está acima da média!</p>`;

    resultado.appendChild(box);
  }

  // Média total
  let mediaTotal = medias.reduce((a,b)=>a+b,0)/medias.length;
  let finalBox = document.createElement("div");
  finalBox.className = "result-box final show";
  finalBox.innerHTML = `<h3>Média geral: ${mediaTotal.toFixed(2)}</h3>`;

  if (bimestre === 4) {
    if (mediaTotal < 7) finalBox.innerHTML += `<p>❌ Infelizmente, você ficou de recuperação.</p>`;
    else finalBox.innerHTML += `<p>🎉 Parabéns, você passou de ano!</p>`;
  }

  resultado.appendChild(finalBox);
});