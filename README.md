# 🇵🇹 Portugal District Game

Um mini‑jogo interativo criado com **Python Turtle** onde o jogador tenta adivinhar todos os distritos de Portugal, escrevendo os nomes diretamente numa imagem‑mapa. À medida que o utilizador acerta, os distritos são marcados no mapa; quando termina ou escreve *exit*, o jogo mostra também os distritos que ficaram por adivinhar.

---

## 🎯 Objetivo do Jogo

- Adivinhar todos os distritos de Portugal.
- Cada resposta correta é escrita no mapa na posição correspondente.
- O jogador pode terminar a qualquer momento escrevendo **exit**.
- No final, os distritos não adivinhados são mostrados a vermelho e guardados num ficheiro CSV.

---

## 🧠 Funcionalidades Principais

- Interface gráfica com **Python Turtle**.
- Mapa de Portugal carregado como imagem de fundo.
- Leitura de coordenadas e nomes a partir de um ficheiro CSV.
- Escrita dos distritos corretos no mapa (a verde).
- Geração automática de um ficheiro `districts_failed.csv` com os distritos não adivinhados.
- Visualização no mapa dos distritos falhados (a vermelho).
- Possibilidade de terminar o jogo a qualquer momento com o comando **exit**.

---

## 📁 Estrutura dos Dados

O projeto utiliza dois ficheiros CSV:

- **districts.csv**  
  Contém todos os distritos, com respetivas coordenadas no mapa.

- **districts_failed.csv**  
  Gerado automaticamente quando o jogador termina com *exit*.  
  Inclui apenas os distritos que não foram adivinhados.