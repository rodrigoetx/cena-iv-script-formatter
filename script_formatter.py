import os

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

def main():
    print("Iniciando Módulo de Leitura - Formatação Cena IV")
    # Apenas como base de teste para o primeiro commit
    pass

if __name__ == "__main__":
    main()
