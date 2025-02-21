# WhatsApp-bot-mensagens
Este script automatiza o envio de mensagens pelo WhatsApp Web. Ele lê os números de um arquivo JSON, abre o WhatsApp no Chrome e usa PyAutoGUI para clicar, digitar e enviar a mensagem automaticamente.


## Tecnologias Utilizadas  
- Python  → Linguagem principal do script  

- webbrowser → Abre links no navegador  

- pyautogui → Simula cliques e digitação  

- json → Lê os números de um arquivo externo 

- time → Controla os intervalos entre as ações  

## Como Usar  
Instale as dependências necessárias:  
   ```bash
   pip install pyautogui

   ``` 
- Altere números do arquivo telefones.json. O arquivo já contém exemplos com números inválidos.

- Caso o WhatsApp Web não esteja carregando corretamente, verifique se o navegador está atualizado.

- O uso excessivo deste script pode levar a restrições ou bloqueios no WhatsApp. Utilize com moderação e apenas para fins legítimos.