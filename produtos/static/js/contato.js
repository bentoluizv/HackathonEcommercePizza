document.addEventListener("DOMContentLoaded", function () {
  // Inicialize o EmailJS
  emailjs.init("6n3a4hqovdjs1_p42"); // Substitua pelo seu User ID

  // Capturar o formulário e os elementos
  const form = document.getElementById("contact-form");
  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const messageInput = document.getElementById("message");
  const submitBtn = document.getElementById("submit-btn");

  // Evento de envio do formulário
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = nameInput.value;
    const email = emailInput.value;
    const message = messageInput.value;

    // Validação simples
    if (name === "" || email === "" || message === "") {
      alert("Preencha todos os campos!");
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Enviando...";

    // Parâmetros do template do EmailJS
    const templateParams = {
      from_name: name,
      message: message,
      email: email,
    };

    // Enviar o email usando EmailJS
    emailjs.send("service_4rhm7kk", "template_wc2kdg8", templateParams).then(
      function (response) {
        console.log("Sucesso!", response.status, response.text);
        alert("Email enviado com sucesso!");
        nameInput.value = "";
        emailInput.value = "";
        messageInput.value = "";
        submitBtn.disabled = false;
        submitBtn.textContent = "Enviar";
      },
      function (error) {
        console.error("Erro:", error);
        alert("Falha ao enviar o email. Tente novamente.");
        submitBtn.disabled = false;
        submitBtn.textContent = "Enviar";
      }
    );
  });
});
