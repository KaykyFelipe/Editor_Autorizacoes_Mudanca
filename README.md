

Recentemente, concluí um projeto em Python voltado para a criação de um editor de documentos de autorização de mudança. Esse software é utilizado pela contabilidade/administradora de condomínios onde trabalho atualmente.

O objetivo do programa é gerar um arquivo PDF com base em um modelo fornecido em formato Word. Ele substitui os campos necessários para tornar o documento exclusivo para um morador e um condomínio específico. Além disso, o programa considera que cada condomínio possui regras específicas para horários de mudança.

O processo ocorre da seguinte forma:

* O usuário preenche os dados relevantes para a autorização de mudança .
* Após a coleta das informações, um relatório é exibido para que o usuário confirme os dados digitados.
* Ao pressionar a tecla “ENTER”, o programa gera a autorização de mudança em PDF (Nomeando o arquivo de acordo com o condominio, unidade, motivo).
* O arquivo PDF gerado é salvo em um diretório específico. Cada condomínio tem seu próprio diretório, configurado previamente em um arquivo TXT que armazena o diretorio exclusivo (O caminho também pode ser editado, pois os diretorios estão disponiveis na pasta local do programa).


