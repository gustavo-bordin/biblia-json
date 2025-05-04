# 📖 biblia-json

**Coleção de versões da Bíblia em formato JSON**, organizadas para fácil acesso e uso em aplicações de qualquer natureza. Também inclui os scripts em Python utilizados no processo de conversão e formatação dos textos.

## 📂 Conteúdo

Atualmente, este repositório contém:

- **KJV (King James Version)** em formato JSON  
- Scripts Python usados para gerar e organizar os arquivos

## 💡 Objetivo

Este projeto tem como objetivo fornecer versões da Bíblia em formato estruturado, prontas para uso em **qualquer tipo de aplicações**.

## 🛠 Estrutura dos Dados

Cada versão da Bíblia segue a seguinte estrutura JSON:

```json
{
  "slug": "KJV",
  "name": "King James",
  "version": "1611",
  "books": [
    {
      "name": "Genesis",
      "chapters": [
        {
          "name": "Capítulo 1",
          "number": 1,
          "verses": [
            {
              "number": 1,
              "text": "In the beginning God created the heaven and the earth."
            },
            {
              "number": 2,
              "text": "And the earth was without form, and void; and darkness was upon the face of the deep..."
            }
            // ...
          ]
        }
        // ...
      ]
    }
    // ...
  ]
}

## 🔁 Níveis de estrutura:

- `slug`: identificador da versão (ex: `"KJV"`)  
- `name`: nome da versão (ex: `"King James"`)  
- `version`: ano ou código da versão (ex: `"1611"`)  
- `books`: lista de livros  
  - `name`: nome do livro (ex: `"Genesis"`)  
  - `chapters`: lista de capítulos  
    - `name`: nome do capítulo (ex: `"Capítulo 1"`)  
    - `number`: número do capítulo  
    - `verses`: lista de versículos  
      - `number`: número do versículo  
      - `text`: texto do versículo  

## 📜 Licença

- O conteúdo da Bíblia KJV está em domínio público.  
- Os scripts Python são disponibilizados sob a [Licença MIT](LICENSE).

## 🚧 Futuro

- Inclusão de outras versões da Bíblia  
- Melhorias nos scripts de processamento  
- Suporte a múltiplos idiomas  

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
