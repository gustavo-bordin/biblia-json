# 📖 Biblia JSON

**Coleção de versões da Bíblia em formato JSON**, organizadas para fácil acesso e uso em aplicações de qualquer natureza. 
Também inclui os scripts em Python utilizados no processo de conversão e formatação dos textos.

-- 

### 📂 Conteúdo

Atualmente, este repositório contém:

- **KJV (King James Version)** em formato JSON  
- Scripts Python usados para gerar e organizar os arquivos

--

### 💡 Objetivo

Este projeto tem como objetivo fornecer versões da Bíblia em formato estruturado, prontas para uso em **qualquer tipo de aplicações**.

--

### 🛠 Estrutura dos Dados

Cada versão da Bíblia segue a seguinte estrutura JSON:

```json
{
  "slug": "",  // Identificador da versão
  "name": "",  // Nome da versão
  "version": "",  // Ano ou código da versão
  "books": [  // Lista de livros
    {
      "name": "",  // Nome do livro
      "chapters": [  // Lista de capítulos
        {
          "name": "",  // Nome do capítulo
          "number": 1,  // Número do capítulo
          "verses": [  // Lista de versículos
            {
              "number": 1,  // Número do versículo
              "text": ""  // Texto do versículo
            }
          ]
        }
      ]
    }
  ]
}
```

--

### 📜 Licença

- O conteúdo da Bíblia KJV está em domínio público.  
- Os scripts Python são disponibilizados sob a [Licença MIT](LICENSE).

--

### 🚧 Futuro

- Inclusão de outras versões da Bíblia  
- Melhorias nos scripts de processamento  
- Suporte a múltiplos idiomas
  
