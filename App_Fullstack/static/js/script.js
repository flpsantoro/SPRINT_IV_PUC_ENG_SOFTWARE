document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const resultDiv = document.getElementById('uploadResult');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData();
        const modelFile = document.getElementById('modelFile').files[0];
        formData.append('modelFile', modelFile);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = 'Resultado do Upload: ' + data.message;
        })
        .catch(error => {
            console.error('Erro no upload:', error);
            resultDiv.innerHTML = 'Erro no upload do arquivo.';
        });
    });
});
