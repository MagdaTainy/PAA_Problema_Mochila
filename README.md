# Seminário 2 – Projeto e Análise de Algoritmos  
## Problema da Mochila 

### 🎯 Equipe  
- Magda Tainy Nunes Amaral
- Cesar Mateus Trindade

---

### 🧩 Descrição do Projeto  
Este projeto aborda o **Problema da Mochila 0/1** (Knapsack Problem), que consiste em:  
> Dado um conjunto de itens, cada um com valor \(v_i\) e peso \(w_i\), e uma mochila com capacidade \(W\), selecionar quais itens incluir de modo a maximizar o valor total sem exceder a capacidade.  

O problema pertence à classe **NP-Completo** e será abordado por duas técnicas de construção de algoritmo:  
- **Programação Dinâmica (PD)** — para obter a solução ótima.  
- **Heurística Gulosa** — para obter uma solução aproximada rápida, baseada na razão valor/peso.  

---

### 🛠 Implementação  
O repositório inclui:  
- `knapsack_problem.py` — código em Python com as duas abordagens (PD e gulosa).  
- `Seminario2_Problema_da_Mochila.pdf` — relatório do seminário com definição do problema, técnica, código e dataset simples.  

#### Como executar  
1. Certifique-se de ter Python 3 instalado.  
2. No terminal, navegue até a pasta do projeto.  
3. Execute:  
   ```bash
   python knapsack_problem.py

Ou acessar o notebook no colab:
https://colab.research.google.com/drive/1QN2MkeLgRuso9uVCoQ5z6LprEHVT-6Tt?usp=sharing

📊 Dataset simples
Valores dos itens: [60, 100, 120, 90, 30]
Pesos dos itens: [10, 20, 30, 25, 15]
Capacidade da mochila: 50
Exemplo de instância:
Itens 1 a 5 com os valores e pesos acima.
Objetivo: maximizar valor sem ultrapassar peso 50.
Resultados esperados:
Programação Dinâmica → Valor máximo = 220
Heurística Gulosa → Valor aproximado = 190

📌 Conclusão

Esse trabalho evidencia a diferença entre técnicas de resolução de problemas NP-Completos:
A Programação Dinâmica fornece a solução ótima, com complexidade O(n * W).

A Heurística Gulosa oferece uma solução rápida com complexidade O(n log n), mas sem garantia de ótimo.
Assim, o projeto demonstra o equilíbrio entre precisão e eficiência em algoritmos de otimização.

📁 Estrutura do Repositório

/
├── knapsack_problem.py
├── Seminario2_Problema_da_Mochila.pdf
└── README.md


🎥 Vídeo de Apresentação
https://www.youtube.com/watch?v=vHpFtDH_E2s

📚 Referências

Weiss, M. A. Data Structures & Algorithm Analysis in C++.

Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. Introduction to Algorithms (3ª ed.).

Texto sobre o problema da mochila 0/1 em sites acadêmicos de algoritmos.
   
