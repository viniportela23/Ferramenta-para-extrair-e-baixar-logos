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
  const rows = document.querySelectorAll('tr[role="row"]');
  const channelsWithoutImage = [];

  rows.forEach((row) => {
    const imageElement = row.querySelector('td.dt-center a img');
    
    // Se não houver imagem, extrai o nome do canal
    if (!imageElement) {
      const nameElement = row.querySelector('td:nth-child(3) a strong');
      const name = nameElement ? nameElement.textContent.trim() : '';
      channelsWithoutImage.push(name);
    }
  });

  const channelNames = channelsWithoutImage.join("\n");

  // Agora você pode fazer o que quiser com os dados extraídos.
  // Neste exemplo, vamos criar um link de download na página.
  const downloadLink = document.createElement("a");
  downloadLink.href = "data:text/plain;charset=utf-8," + encodeURIComponent(channelNames);
  downloadLink.download = "channels_without_image.txt";
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);
  downloadLink.click();

  // Remover o link após o download
  document.body.removeChild(downloadLink);
}
