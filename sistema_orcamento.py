# Erik dos Santos Sousa
# ADS-EAD
# RA - 151230

from class_apoio import *


def executar_locacao(tipo_locacao):
    nome, cpf = coletar_dados_cliente()
    resumo = ORCAMENNTO(nome, cpf, tipo_locacao.upper())
    resumo.valor_aluguel += PRECOS[tipo_locacao]

    if tipo_locacao != "Estudio":
        while True:
            exibir_cabecalho("DETALHES DO IMÓVEL: DORMITÓRIOS")
            print(f"1-Quarto\n2-Quartos(+ R$ {'200.00' if tipo_locacao == 'Apartamento' else '250.00'})")
            qtd_quartos = input("\nEscolha uma Opção (1 ou 2): ").strip()
            if qtd_quartos == "1":
                break
            elif qtd_quartos == '2':
                resumo.valor_aluguel += 200.00 if tipo_locacao == "Apartamento" else 250.00
                resumo.detalhes.append("2 Quartos")
                break
            else:
                print(f"{Fore.RED}⚠️ Opção inválida! Escolha 1 ou 2.{Style.RESET_ALL}")
                input("Pressione ENTER para tentar novamente...")

        while True:
            exibir_cabecalho("DETALHES DO IMÓVEL: GARAGEM")
            vaga = input("Deseja Vaga por R$300.00? (1-Sim / 2-Não):") .strip()
            if vaga == '1':
                resumo.valor_aluguel += 300.00
                resumo.detalhes.append("Com Garagem")
                break
            elif vaga == '2':
                break
            else:
                print(f"{Fore.RED}⚠️ Opção inválida! Escolha 1 ou 2.{Style.RESET_ALL}")
                input("Pressione ENTER para tentar novamente...")

    else:
        while True:    
            exibir_cabecalho("DETALHES DO IMÓVEL: VAGAS (ESTÚDIO)")
            print(f"{Fore.CYAN}🌟 CONDIÇÃO ESPECIAL: 2 vagas por R$ 250,00.{Style.RESET_ALL}")
            print(f"As demais vagas saem por R$ 60,00 cada.")
            
            vaga_padrao = input("\nDeseja contratar o pacote de 2 vagas padrão? (1-Sim / 2-Não): ").strip()
            
            if vaga_padrao == '1':
                resumo.valor_aluguel += 250.00
                resumo.detalhes.append("2 Vagas (Condição Especial)")
                
               
                while True:
                    try:
                        vaga_extra = int(input("Deseja adicionar mais vagas extras (R$ 60,00 cada)? (Digite 0 para não): "))
                        if vaga_extra >= 0:
                            if vaga_extra > 0:
                                resumo.valor_aluguel += (vaga_extra * 60.00)
                                resumo.detalhes.append(f"{vaga_extra} Vaga(s) Extra(s)")
                            print(f"{Fore.GREEN}✅ Vagas configuradas com sucesso!{Style.RESET_ALL}")
                            break
                        else:
                            print(f"{Fore.RED}⚠️ Por favor, digite um número positivo.{Style.RESET_ALL}")
                    except ValueError:
                        print(f"{Fore.RED}⚠️ Erro: Digite apenas o NÚMERO de vagas (ex: 1, 2, 3).{Style.RESET_ALL}")
                
                break
                
            elif vaga_padrao == '2':
                print(f"{Fore.YELLOW}ℹ️ Prosseguindo sem vagas de garagem para o Estúdio.{Style.RESET_ALL}")
                break 
            else:
                print(f"{Fore.RED}⚠️ Opção inválida! Escolha 1 para Sim ou 2 para Não.{Style.RESET_ALL}")
                input("Pressione ENTER para tentar novamente...")

    if tipo_locacao == "Apartamento":
        while True:
            exibir_cabecalho("DETALHES DO IMÓVEL:INFORMAÇÕES ADICIONAIS")
            crianca = input("Possui Crianças? (1-sim / 2-Não): ")
            if crianca == '2':
                resumo.valor_aluguel *=0.95
                resumo.detalhes.append("Desc. 5% (Sem Criança)")
                break
            elif crianca == '1':
                resumo.detalhes.append("Com Criança")
                break
            else:
                print(f"{Fore.RED}⚠️ Opção inválida! Escolha 1 ou 2.{Style.RESET_ALL}")
                input("Pressione ENTER para tentar novamente...")

    while True:
        exibir_cabecalho("PAGAMENTO - PARCELAMENTO CONTRATO")
        print("Valor do Contrato Imóbiliario: R$ 2000.00")
        print("=" * 100)
        try:
            parcelamento = input("Deseja parcelar o contrato imobiliário? (Parcelamento disponível em até 5x)\n(1-Sim/2-Não): ").strip()
            if parcelamento == '1':
                qtd_parcelas = int(input("Quantidade de parcelas? (Máximo 5x): "))
                if 1 <= qtd_parcelas <= 5:
                    resumo.parcela_contrato =qtd_parcelas
                    resumo.valor_contrato_mensal = 2000.00 / qtd_parcelas 
                    print(f"{Fore.GREEN}✅ Contrato Parcelamento em {qtd_parcelas}x.{Style.RESET_ALL}")
                    break
                else:
                    print("Quantidade de parcelas inválida!")

            elif parcelamento == '2':
                resumo.parcela_contrato = 1
                resumo.valor_contrato_mensal = 2000.00
                print("Pagamento à vista configurada")
                break
            else:
                print(f"{Fore.RED}⚠️ O limite é de 1 a 5 parcelas.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}⚠️ Erro! Digite apenas números inteiros.{Style.RESET_ALL}")
        input("Pressione ENTER para tentar novamente...")

    while True:
        exibir_cabecalho("PAGAMENTO - RESUMO DO ORÇAMENTO")
        print(f"Locatário: {resumo.nome} | CPF: {resumo.cpf}")
        print(F"Imóvel: {resumo.tipo_locacao} | {' | '.join(resumo.detalhes)}") 
        print("=" * 100)
        print(f"Aluguel Mensal: R${resumo.valor_aluguel:.2f} ")
        print(f"Contrato: {resumo.parcela_contrato}x de R$ {resumo.valor_contrato_mensal:.2f}")
        print("=" * 100)
        print(f"{Fore.GREEN}Total mensal inicial: R$ {resumo.calcular_total_inicial():.2f}{Style.RESET_ALL}")
        print("=" * 100)

        Confimar = input(f"\nConfirmar locação e gerar CSV ? (1-Sim/2-Não)").strip().upper( )
        if Confimar == '1':
            arquivo_csv = resumo.gerar_csv()
            locacao_formatada = f"Locação  {resumo.tipo_locacao.upper()} {resumo.nome.upper()}."
            print(f"\n{Fore.GREEN}🏠 Locação concluída com sucesso! O contrato do imóvel foi gerado no arquivo: {locacao_formatada} {Style.RESET_ALL}\n")
            break
        elif Confimar == '2':
            print(f"\n{Fore.YELLOW}⚠ Locação não concluída. A operação foi cancelada.{Style.RESET_ALL}\n")
            break
        else:
            print(f"{Fore.RED}⚠️ Digite apenas S ou N.{Style.RESET_ALL}")
            input("Pressione ENTER...")
    input("Pressione ENTER para retornar ao menu.")        
                  
def menu():
     while True:
        exibir_cabecalho("SISTEMA R.M LOCAÇÕES")
        print("1 - Apartamento\n2 - Casa\n3 - Estudio\n4 - Sair")
        opcao = input("\nSelecione uma locação: ")
        if opcao =='1':
            executar_locacao("Apartamento")
        elif opcao == '2': 
            executar_locacao("Casa")
        elif opcao == '3': 
            executar_locacao("Estudio")
        elif opcao == '4': 
            print(f"\n{Fore.CYAN}Encerrando sistema... Até logo!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}🛑 Opção Inválida!{Style.RESET_ALL}")
            input("Pressione ENTER...")
            

    
            
if __name__  == "__main__":
    menu()










        
   