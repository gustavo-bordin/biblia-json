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
  "slug": "KJV",  // Identificador da versão (ex: "KJV")
  "name": "King James",  // Nome da versão (ex: "King James")
  "version": "1611",  // Ano ou código da versão (ex: "1611")
  "books": [  // Lista de livros
    {
      "name": "Genesis",  // Nome do livro (ex: "Genesis")
      "chapters": [  // Lista de capítulos
        {
          "name": "Capítulo 1",  // Nome do capítulo (ex: "Capítulo 1")
          "number": 1,  // Número do capítulo (ex: 1)
          "verses": [  // Lista de versículos
            {
              "number": 1,  // Número do versículo (ex: 1)
              "text": "In the beginning God created the heaven and the earth."  // Texto do versículo
            }
          ]
        }
      ]
    }
  ]
}
```

## 📜 Licença

- O conteúdo da Bíblia KJV está em domínio público.  
- Os scripts Python são disponibilizados sob a [Licença MIT](LICENSE).

## 🚧 Futuro

- Inclusão de outras versões da Bíblia  
- Melhorias nos scripts de processamento  
- Suporte a múltiplos idiomas
  
