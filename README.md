# Cena IV Script Formatter 🎭

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FPDF](https://img.shields.io/badge/Library-FPDF2-red?style=for-the-badge)

Um motor de exportação desenvolvido exclusivamente para a **Cena IV Shakespeare Cia.**, com o objetivo de otimizar os processos internos de produção teatral unindo tecnologia da informação e artes cênicas.

## Objetivo Estratégico
Roteiristas e diretores teatrais frequentemente trabalham com textos brutos de edição rápida (em formato TXT). No entanto, fornecer um arquivo sem hierarquia visual para os atores atrasa o ritmo dos ensaios, pois a transição de olhar entre **Falas** e **Rubricas de Palco** precisa ser instantânea.

O *Script Formatter* resolve esse gargalo produtivo: ele analisa hierarquicamente um texto bruto e exporta um arquivo `.pdf` parametrizado, desenhado especialmente para leitura sob baixa luminosidade nas coxias ou em tablets digitais no palco.

## Características Técnicas
- **Leitura Orientada a Objetos (OOP):** O sistema isola a lógica de extração sintática (Parser) da lógica de rasterização PDF (Generator), permitindo que a Cia. inclua outros formatos de saída no futuro.
- **Tipografia Dinâmica:** Nomes em negrito, rubricas em itálico e espaçamento controlado.
- **Recuo Automático:** Identação natural para rubricas de palco `pdf.set_x(30)` melhorando imediatamente a escaneabilidade dos scripts.
- **Cabeçalhos Formais:** Todos os documentos gerados mantêm o padrão oficial e profissional da Cena IV.

## Como Executar
Disponha do ambiente Python e instale a dependência de PDF (`fpdf2`):

```bash
pip install fpdf2
python script_formatter.py
```

O arquivo `ensaio_sample.txt` será processado e o sistema gerará o arquivo formatado em PDF no mesmo diretório.

---
*Developed by Rodrigo Espinosa - Systems Analysis & Development*
