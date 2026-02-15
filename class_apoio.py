import os
import csv
import colorama
from colorama import Fore, Style
from datetime import datetime

colorama.init(autoreset=True)


class ORCAMENNTO:
    def __init__(self, nome, cpf, tipo_locacao):
        self.nome = nome
        self.cpf = cpf
        self.tipo_locacao = tipo_locacao
        self.valor_aluguel = 0.0
        self.detalhes = []
        self.parcela_contrato = 0
        self.valor_contrato_mensal = 0.0

    def calcular_total_inicial(self):
        return self.valor_aluguel + self.valor_contrato_mensal 

    def gerar_csv(self):
        diretorio_saida = "Contratos_Gerados"
        if not os.path.exists(diretorio_saida):
            os.makedirs(diretorio_saida)
        agora = datetime.now().strftime("%d-%m-%Y _ %H-%M")

        nome_arquivo = os.path.join(diretorio_saida, f"Contrato - '{self.tipo_locacao}' {self.nome} {agora}.csv")
    
        meses_lista = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as ficheiro:
            escritor = csv.writer(ficheiro)
            escritor.writerow(['SISTEMA R.M LOCAÇÃO - CRONOGRAMA DE PAGAMENTO'])
            escritor.writerow(['CLIENTE', self.nome, 'CPF', self.cpf,'IMÓVEL', self.tipo_locacao])
            escritor.writerow(['DETALHES', " | ".join(self.detalhes)])      
            escritor.writerow(['MÊS','ALUGUEL (R$)', 'CONTRATO (R$)', 'TOTAL(R$)'])


            for i in range(1, 13):
                parcela_contrato_atual = self.valor_contrato_mensal if i <= self.parcela_contrato else 0.0
                total_mes = self.valor_aluguel + parcela_contrato_atual
                escritor.writerow([
                    meses_lista[i-1],
                    f"{self.valor_aluguel:.2f}", 
                    f"{parcela_contrato_atual:.2F}",
                    f"{total_mes:.2f}"
            ])



PRECOS = {
    "Apartamento": 700.00,
    "Casa": 900.00,
    "Estudio": 1200.00,
    "Contrato": 2000.00,
    "Vaga_Extra": 60.00}

def limpar_tela():     
    print("\033c", end ="")

def exibir_cabecalho(titulo):
    limpar_tela()
    print(f"{Fore.CYAN}{'=' * 55}")
    print(f"{Style.BRIGHT}{'SISTEMA DE LOCAÇÃO - IMOBILIÁRIA R.M'.center(55)}")
    print(f"{titulo.center(55)}{Style.NORMAL}")
    print(f"{Fore.CYAN}{'=' * 55}{Style.RESET_ALL}\n")

def coletar_dados_cliente():
    while True:
        limpar_tela()
        exibir_cabecalho("CADASTRO DO CLIENTE")
        nome = input("Nome Completo: ").strip().upper()
        cpf_input = input(f"CPF: ").strip()
        cpf_numeros = "".join(filter(str.isdigit, cpf_input))
        if len(cpf_numeros) == 11:
            cpf_formatado =f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
            if nome:
                return nome, cpf_formatado
        print(f"{Fore.RED}⚠️ Nome e CPF são obrigatórios!{Style.RESET_ALL}")
        input("Pressione ENTER para tentar novamente...")
        return coletar_dados_cliente()



