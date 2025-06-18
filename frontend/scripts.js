async function summarizeText() {
    const text = document.getElementById("inputText").value;
    const formData = new FormData();
    formData.append("text", text);

    const response = await fetch("http://127.0.0.1:8000/summarize/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.summary;
}