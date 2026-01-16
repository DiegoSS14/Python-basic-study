# Python Basic Study 💻🐍

**Estudo geral sobre a linguagem Python**. Este repositório reúne exercícios e pequenos projetos usados durante o aprendizado dos fundamentos da linguagem, conceitos de orientação a objetos e o uso de algumas bibliotecas populares do ecossistema Python (por exemplo: **pandas**, **numpy**, **matplotlib** e módulos para estudo de IA).

---

## 🚀 Visão geral

- Objetivo: organizar e documentar exercícios práticos para fixar conceitos de Python. 
- Público: pessoas que estão começando ou revisando fundamentos de Python.

---

## 📚 Conteúdo e tópicos estudados

**Fundamentos da linguagem**
- Tipos e variáveis, operações básicas
- Estruturas condicionais (`if`, `match`) — veja `basic/condicao`
- Laços de repetição (`for`, `while`) — veja `basic/repeticao`
- Funções e função anônima (lambda), filter — veja `basic/funcoes` e `basic/funcaoAnonima`
- Tratamento de exceções — veja `basic/excecao`
- Leitura e escrita de arquivos (`.txt`, `.csv`, `.json`) — veja `basic/arquivos`

**Estruturas de dados**
- Listas, coleções e matrizes — veja `basic/listasEmatrizes`
- Recursão — veja `basic/recursividade`

**Orientação a Objetos (OOP)**
- Classes, construtores e instâncias — exemplos em `orientacaoAObjetos/produto/Produto.py`
- Herança, polimorfismo e encapsulamento — veja `orientacaoAObjetos/*`
- Composição, métodos especiais, métodos estáticos e de classe

**Bibliotecas e exemplos práticos**
- `bibliotecas/externalLibs/libPandas.py` — introdução a **pandas**
- `bibliotecas/externalLibs/libNumpy.py` — introdução a **numpy**
- `bibliotecas/externalLibs/libMatPlot.py` — exemplos com **matplotlib**
- Pastas `examples/` e `bibliotecas/` contêm scripts de apoio e estudos aplicados (finanças, marketing, etc.)

---

## 🧪 Como executar

1. Tenha o Python 3.10+ instalado.
2. Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
```

3. Instale as dependências (caso queira executar scripts que usam bibliotecas externas):

```bash
pip install pandas numpy matplotlib
```

4. Execute scripts diretamente, por exemplo:

```bash
python basic/funcoes/calculadora.py
python orientacaoAObjetos/produto/Produto.py
```

> Dica: navegue pelas pastas e abra os arquivos para entender a implementação de cada exercício.

---

## 📁 Estrutura do repositório (resumo)

- `basic/` — exercícios de sintaxe, estruturas, arquivos, funções
- `bibliotecas/` — estudos com bibliotecas externas
- `examples/` — pequenos scripts de aplicação
- `orientacaoAObjetos/` — exemplos de classes e conceitos OOP

---

## 🤝 Contribuições

Este repositório é principalmente um caderno de estudos. Pull requests com correções de português, melhorias de exemplos ou novas seções são bem-vindas. Favor manter a proposta educacional e clara no código.

---

## ✍️ Nota final

Projeto criado para aprendizado pessoal e ensino prático de conceitos básicos e intermediários de Python. Use-o livremente para estudo e referência.

