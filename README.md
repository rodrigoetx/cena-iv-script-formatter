# Cena IV Script Formatter 🎭

Fala galera! Desenvolvi esse motor de formatação de roteiros para ajudar a agilizar nossos processos internos lá na **Cena IV Shakespeare Cia**. 

A ideia aqui é testar algumas propostas tecnológicas para o nosso dia a dia no teatro, unindo ferramentas de TI com as nossas artes cênicas.

## Por que eu fiz isso?
A gente sabe que ler texto cru (TXT ou Word sem formatação pesada) de roteiro na hora do ensaio é complicado, ainda mais com luz baixa ou dividindo cena. A transição rápida de olhar entre **Falas** e **Ação (Rubrica)** precisa ser nítida pra não quebrar o ritmo.

Então criei esse *Script Formatter*: ele pega um texto bruto e gera um `.pdf` super profissional, já com Capa Oficial, margens adequadas para segurar a folha/tablet, nomes em negrito e rubricas em itálico recuadas na cor cinza. Fica muito mais fácil de ler e absorver.

## O que vem pela frente?
Isso é só a fase 1 das minhas propostas. Futuramente, estou pensando em implementar um sistema de **OCR (Reconhecimento Óptico de Caracteres)** com IA. Assim, a gente vai poder tirar foto de um roteiro impresso antigo e o sistema converte direto pro PDF formatadinho!

## Como testar
Se você tem o Python instalado (e a lib `fpdf2`), é só rodar no terminal:

```bash
pip install fpdf2
python script_formatter.py
```

Ele vai ler o arquivo de exemplo (`ensaio_sample.txt`) e gerar um arquivo `roteiro_ensaio.pdf` lindão no mesmo momento. Pode testar!

---
*Developed by Rodrigo Espinosa - Systems Analysis & Development*
