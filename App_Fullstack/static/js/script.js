document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Coleta os dados dos checkboxes
        const formData = {
            hair: document.getElementById('hair').checked ? 1 : 0,
            feathers: document.getElementById('feathers').checked ? 1 : 0,
            // Repita para os outros checkboxes
        };

        // Envia a solicitação para o backend
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = 'Predição: ' + data;
        })
        .catch(error => {
            console.error('Erro na solicitação:', error);
            resultDiv.innerHTML = 'Erro ao obter predição.';
        });
    });
});
