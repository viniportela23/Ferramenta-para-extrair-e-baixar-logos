chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  if (message.action === "extractedNames") {
    const names = message.data.join("\n\n");
    const filename = "extracted_names.txt";

    const blob = new Blob([names], { type: "text/plain" });
    const url = URL.createObjectURL(blob);

    const downloadLink = document.createElement("a");
    downloadLink.href = url;
    downloadLink.download = filename;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();

    // Remover o link e revogar a URL do objeto Blob após o download
    document.body.removeChild(downloadLink);
    URL.revokeObjectURL(url);
  }
});
