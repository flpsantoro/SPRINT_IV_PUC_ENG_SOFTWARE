document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = {
            hair: document.getElementById('hair').checked ? 1 : 0,
            feathers: document.getElementById('feathers').checked ? 1 : 0,
            eggs: document.getElementById('eggs').checked ? 1 : 0,
            milk: document.getElementById('milk').checked ? 1 : 0,
            airborne: document.getElementById('airborne').checked ? 1 : 0,
            aquatic: document.getElementById('aquatic').checked ? 1 : 0,
            predator: document.getElementById('predator').checked ? 1 : 0,
            toothed: document.getElementById('toothed').checked ? 1 : 0,
            backbone: document.getElementById('backbone').checked ? 1 : 0,
            breathes: document.getElementById('breathes').checked ? 1 : 0,
            venomous: document.getElementById('venomous').checked ? 1 : 0,
            fins: document.getElementById('fins').checked ? 1 : 0,
            legs: Math.max(0, (parseInt(document.getElementById('legs').value) || 1) - 1),
            tail: document.getElementById('tail').checked ? 1 : 0,
            domestic: document.getElementById('domestic').checked ? 1 : 0,
            catsize: document.getElementById('catsize').checked ? 1 : 0
        };

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
            clearForm();
        })
        .catch(error => {
            console.error('Erro na solicitação:', error);
            resultDiv.innerHTML = 'Erro ao obter predição.';
        });
    });

    function clearForm() {
        document.getElementById('hair').checked = false;
        document.getElementById('feathers').checked = false;
        document.getElementById('eggs').checked = false;
        document.getElementById('milk').checked = false;
        document.getElementById('airborne').checked = false;
        document.getElementById('aquatic').checked = false;
        document.getElementById('predator').checked = false;
        document.getElementById('toothed').checked = false;
        document.getElementById('backbone').checked = false;
        document.getElementById('breathes').checked = false;
        document.getElementById('venomous').checked = false;
        document.getElementById('fins').checked = false;
        document.getElementById('legs').value = '';
        document.getElementById('tail').checked = false;
        document.getElementById('domestic').checked = false;
        document.getElementById('catsize').checked = false;
    }
});
