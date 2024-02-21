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
// content.js

// Função para extrair os dados da página
function extractData() {
    const rows = document.querySelectorAll('tr[role="row"]');
    const channelsWithoutImage = [];

    rows.forEach((row) => {
        const urlElement = row.querySelector('td:nth-child(4) a');
        let url = urlElement ? urlElement.href : '';

        const nameElement = row.querySelector('td:nth-child(3) a strong');
        const name = nameElement ? nameElement.textContent.trim() : '';

        // Modificação: Capturando o link da imagem, se disponível
        const imageLinkElement = row.querySelector('td:nth-child(2) a img');
        let imageLink = imageLinkElement ? imageLinkElement.src : '';

        // Remover a parte específica da URL
        imageLink = imageLink.replace('http://185.236.183.106/GnVfEmsv/resize?maxw=96&maxh=32&url=', '');

        // Decodificar a URL para o formato convencional
        imageLink = decodeURIComponent(imageLink);

        channelsWithoutImage.push({ name, url, imageLink });
    });

    // Formata os dados para o arquivo de texto
    let dataToSave = channelsWithoutImage.map(channel => `${channel.name} - ${channel.imageLink}`).join("\n");

    // Aplicar filtragem após todo o texto ter sido gerado
    dataToSave = dataToSave.split('\n').filter(line => !line.includes('rochagalaxia.live')).join('\n');

    // Cria e baixa o arquivo de texto
    const downloadLink = document.createElement("a");
    downloadLink.href = "data:text/plain;charset=utf-8," + encodeURIComponent(dataToSave);
    downloadLink.download = "channels_without_rochagalaxia.txt";
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();

    // Remove o link após o download
    document.body.removeChild(downloadLink);
}

// Inicia a extração de dados quando a página estiver carregada
extractData();
