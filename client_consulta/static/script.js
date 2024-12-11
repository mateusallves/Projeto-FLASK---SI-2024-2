document.getElementById('search-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const cpf = document.getElementById('cpf').value;

    const resposta = await fetch(`/consulta/${cpf}`);
    const dados = await resposta.json();

    const informacoesDoCliente = document.getElementById('client-info');
    informacoesDoCliente.innerHTML = '';

    if (dados.error) {
        informacoesDoCliente.innerHTML = `<div class="alert alert-danger">${dados.error}</div>`;
    } else {
        informacoesDoCliente.innerHTML = `
            <h4>Dados do Cliente:</h4>
            <p><strong>Nome:</strong> ${dados.nome}</p>
            <p><strong>Data de Nascimento:</strong> ${dados.nascimento}</p>
            <p><strong>E-mail:</strong> ${dados.email}</p>
        `;
    }
});

document.getElementById('registration-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const cpf = document.getElementById('novo_cpf').value;
    const nome = document.getElementById('novo_nome').value;
    const nascimento = document.getElementById('novo_nascimento').value;
    const email = document.getElementById('novo_email').value;

    const response = await fetch('/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cpf, nome, nascimento, email }),
    });

    const data = await response.json();
    const registrationMessage = document.getElementById('registration-message');
    registrationMessage.innerHTML = '';

    if (data.success) {
        registrationMessage.innerHTML = `<div class="alert alert-success">${data.success}</div>`;
    } else {
        registrationMessage.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
    }
});
