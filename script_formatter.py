import os
from fpdf import FPDF

class ScriptParser:
    """
    Classe responsável por ler o arquivo bruto de texto e interpretá-lo de forma inteligente.
    Separa cabeçalhos, falas de personagens e rubricas de palco.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw_lines = []
        self.parsed_elements = []

    def load_document(self):
        """Lê o script bruto garantindo a codificação correta."""
        if not os.path.exists(self.filepath):
            print(f"[Erro] O arquivo {self.filepath} não foi localizado no diretório.")
            return False
            
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.raw_lines = file.readlines()
        return True

    def process_text(self):
        """
        Processamento central: identifica a estrutura da frase.
        - Rubricas geralmente vêm entre parênteses.
        - Falas iniciam com NOME DO PERSONAGEM seguido de dois pontos (:).
        """
        for line in self.raw_lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('(') and line.endswith(')'):
                self.parsed_elements.append({"type": "rubrica", "content": line})
            elif ':' in line:
                parts = line.split(':', 1)
                personagem = parts[0].strip().upper()
                fala = parts[1].strip()
                self.parsed_elements.append({"type": "dialogo", "personagem": personagem, "fala": fala})
            else:
                self.parsed_elements.append({"type": "texto_livre", "content": line})

    def get_elements(self):
        return self.parsed_elements

class PdfGenerator(FPDF):
    """Template PDF com cabeçalho e rodapé personalizados para a companhia."""
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'CENA IV SHAKESPEARE CIA. - Roteiro Oficial', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()} | Developed by Rodrigo Espinosa - Systems Analysis & Development', align='C')

class ScriptFormatter:
    """Recebe os elementos mapeados e desenha no documento FPDF."""
    def __init__(self, elements):
        self.elements = elements

    def build_pdf(self, output_file="roteiro.pdf"):
        pdf = PdfGenerator()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        for item in self.elements:
            if item["type"] == "rubrica":
                pdf.set_font("helvetica", "I", 11)
                pdf.multi_cell(0, 6, item["content"], new_x="LMARGIN", new_y="NEXT")
            elif item["type"] == "dialogo":
                pdf.set_font("helvetica", "B", 12)
                pdf.cell(0, 6, item["personagem"], new_x="LMARGIN", new_y="NEXT")
                pdf.set_font("helvetica", "", 12)
                pdf.multi_cell(0, 6, item["fala"], new_x="LMARGIN", new_y="NEXT")
            else:
                pdf.set_font("helvetica", "", 11)
                pdf.multi_cell(0, 6, item["content"], new_x="LMARGIN", new_y="NEXT")
            
            pdf.ln(2) # Pequeno espaçamento entre as falas

        pdf.output(output_file)
        print(f"[{output_file}] criado com sucesso.")

def main():
    print("Iniciando Módulo de Leitura - Formatação Cena IV")
    
    # Gerando um txt de exemplo para consumo do parser
    sample_text = "(As luzes se apagam. Som de tempestade.)\nMACBETH: Assim seja feito.\n(Macbeth saca a espada)\nBRUXA: Salve, Rei da Escócia!"
    with open("ensaio_sample.txt", "w", encoding="utf-8") as f:
        f.write(sample_text)

    # Lógica Central
    parser = ScriptParser("ensaio_sample.txt")
    if parser.load_document():
        parser.process_text()
        
        formatter = ScriptFormatter(parser.get_elements())
        formatter.build_pdf("roteiro_ensaio.pdf")

if __name__ == "__main__":
    main()
