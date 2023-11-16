document.addEventListener("DOMContentLoaded", function () {
  const extractButton = document.getElementById("extractData");
  if (extractButton) {
    extractButton.addEventListener("click", function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        const tabId = tabs[0].id;

        chrome.scripting.executeScript({
          target: { tabId: tabId },
          function: extractData,
        });
      });
    });
  } else {
    console.error("O elemento 'extractData' não foi encontrado na página.");
  }
});

function extractData() {
  const rows = document.querySelectorAll('tr[class^="stream-"]');
  const extractedData = [];

  rows.forEach((row) => {
    const idElement = row.querySelector('td.dt-center');
    const id = idElement ? idElement.textContent : '';

    const nameElement = row.querySelector('td b');
    const name = nameElement ? nameElement.textContent : '';

    const imageElement = row.querySelector('td img');
    const hasImage = imageElement ? "sim" : "não";

    if (hasImage === "não") {
      extractedData.push(name); // Apenas o nome do canal
    }
  });

  const channelNames = extractedData.join("\n");

  // Agora você pode fazer o que quiser com os dados extraídos, incluindo a informação da imagem.
  // Neste exemplo, vamos criar um link de download na página.
  const downloadLink = document.createElement("a");
  downloadLink.href = "data:text/plain;charset=utf-8," + encodeURIComponent(channelNames);
  downloadLink.download = "extracted_names.txt";
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);
  downloadLink.click();

  // Remover o link após o download
  document.body.removeChild(downloadLink);
}
