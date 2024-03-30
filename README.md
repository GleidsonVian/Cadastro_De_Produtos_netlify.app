Automação de Preenchimento de Formulário Web com Selenium e Pandas
Este script Python automatiza o preenchimento de um formulário web com dados de uma planilha Excel usando a biblioteca Selenium para controlar o navegador e a biblioteca Pandas para manipulação dos dados da planilha.

Pré-requisitos
Antes de executar este script, certifique-se de ter instalado os seguintes pacotes Python:

Selenium
Pandas
Além disso, é necessário ter o navegador Chrome e o ChromeDriver instalados e adicionados ao PATH do sistema.

Como usar
Clone este repositório ou baixe o arquivo script.py.
Instale as dependências necessárias executando o seguinte comando:
Copy code
pip install selenium pandas
Execute o script com o seguinte comando:
Copy code
python script.py
Uma janela Tkinter será exibida perguntando se deseja iniciar o preenchimento de dados. Clique em "Sim" para começar ou "Cancelar" para encerrar o programa.
O script abrirá um navegador Chrome, acessará o formulário web em https://cadastroprodutos-devaprender.netlify.app/ e preencherá o formulário com os dados da planilha Excel especificada. Os dados serão preenchidos linha por linha, e a cada linha preenchida, um alerta será exibido e aceito automaticamente.
Após o preenchimento de todos os dados da planilha, o navegador será fechado e o programa será encerrado.
Observações
Certifique-se de substituir o caminho do arquivo da planilha Excel (C:\pasta4\Python\projeto site dev aprender\produtos.xlsx) pelo caminho correto do seu arquivo.
Este script utiliza uma interface gráfica simples criada com Tkinter para interação do usuário.
O tempo de espera entre o preenchimento de cada linha e a aceitação do alerta pode ser ajustado conforme necessário na linha time.sleep(0.3) dentro do loop.
O ChromeDriver utilizado deve ser compatível com a versão do navegador Chrome instalada no sistema.
Este script foi desenvolvido com base nas informações fornecidas. Certifique-se de adaptá-lo conforme necessário para atender às suas necessidades específicas.
