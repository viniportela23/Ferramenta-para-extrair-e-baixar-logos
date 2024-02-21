const names = Array.from(document.querySelectorAll('td b')).map(nameElement => nameElement.textContent);

chrome.runtime.sendMessage({ action: "extractedNames", data: names }, function(response) {
  if (chrome.runtime.lastError) {
    console.error("Erro ao enviar mensagem: " + chrome.runtime.lastError);
  } else {
    console.log("Mensagem enviada com sucesso!");
  }
});
