print("--- CORES DE TEXTO E FUNDO ---")
# Cabeçalho
print(
    f"{'Cor':<10} {'Texto Padrão':<15} {'Fundo Padrão':<15} {'Texto Intenso':<15} {'Fundo Intenso':<15}"
)

cores = {
    "Preto": ("30", "40", "90", "100"),
    "Vermelho": ("31", "41", "91", "101"),
    "Verde": ("32", "42", "92", "102"),
    "Amarelo": ("33", "43", "93", "103"),
    "Azul": ("34", "44", "94", "104"),
    "Magenta": ("35", "45", "95", "105"),
    "Ciano": ("36", "46", "96", "106"),
    "Branco": ("37", "47", "97", "107"),
}

for nome, codigos in cores.items():
    txt, back, txt_int, back_int = codigos
    # string de teste
    s_txt = f"\033[{txt}m Texto {txt} \033[m"
    s_back = f"\033[{back}m Fundo {back} \033[m"
    s_txt_int = f"\033[{txt_int}m Texto {txt_int} \033[m"
    s_back_int = f"\033[{back_int}m Fundo {back_int} \033[m"

    print(f"{nome:<10} {s_txt:<24} {s_back:<24} {s_txt_int:<24} {s_back_int:<24}")
