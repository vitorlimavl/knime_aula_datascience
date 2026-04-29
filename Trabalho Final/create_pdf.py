"""
Gera PDF da documentação do Projeto Final
"""

import os
from fpdf import FPDF
from datetime import datetime

# Criar PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# Cores
DARK_BLUE = (31, 78, 121)
LIGHT_GRAY = (240, 240, 240)
TEXT_COLOR = (0, 0, 0)

# Configurar fontes
pdf.set_font('Arial', '', 11)

# ===== PÁGINA 1: CAPA E INFORMAÇÕES =====
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(*DARK_BLUE)
pdf.cell(0, 20, 'Projeto Final', ln=True, align='C')
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 15, 'Deteccao de Notas Falsas', ln=True, align='C')
pdf.cell(0, 15, 'com Redes Neurais', ln=True, align='C')

pdf.set_text_color(*TEXT_COLOR)
pdf.set_font('Arial', '', 11)
pdf.ln(10)

# Informações do Projeto
pdf.set_font('Arial', 'B', 12)
pdf.cell(50, 8, 'Aluno:', ln=False)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, 'Vitor Hugo Vasconcellos de Lima', ln=True)

pdf.set_font('Arial', 'B', 12)
pdf.cell(50, 8, 'Email:', ln=False)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, 'vitor.hugo.9999@gmail.com', ln=True)

pdf.set_font('Arial', 'B', 12)
pdf.cell(50, 8, 'Dataset:', ln=False)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, 'fake_bills.csv', ln=True)

pdf.set_font('Arial', 'B', 12)
pdf.cell(50, 8, 'Data:', ln=False)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, datetime.now().strftime('%d/%m/%Y'), ln=True)

pdf.ln(10)

# Descrição
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, 'Objetivo:', ln=True)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'Desenvolver um modelo de Rede Neural capaz de classificar notas como genuinas ou falsas, utilizando as medidas fisicas das notas (diagonal, altura, margem, comprimento). O modelo deve ser treinado e avaliado utilizando o framework KNIME.')

pdf.ln(5)

# ===== PÁGINA 2: DATASET E PRÉ-PROCESSAMENTO =====
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*DARK_BLUE)
pdf.cell(0, 10, '1. DATASET E PRE-PROCESSAMENTO', ln=True, border=0)
pdf.set_text_color(*TEXT_COLOR)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '1.1 Caracteristicas do Dataset', ln=True)
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5,
'O dataset fake_bills.csv contem 1.500 registros de medidas fisicas de notas de dinheiro, com a seguinte composicao:\n\n' +
'- Total de registros: 1.500\n' +
'- Classes: 1.000 notas genuinas (66,7%) e 500 notas falsas (33,3%)\n' +
'- Features: 6 medidas fisicas\n' +
'- Valores faltantes: 37 (na coluna margin_low)')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n1.2 Features (Variaveis de entrada)', ln=True)

features_data = [
    ['Diagonal', 'Diagonal da nota'],
    ['Height_left', 'Altura esquerda da nota'],
    ['Height_right', 'Altura direita da nota'],
    ['Margin_low', 'Margem inferior (37 valores faltantes)'],
    ['Margin_up', 'Margem superior'],
    ['Length', 'Comprimento da nota']
]

pdf.set_font('Arial', 'B', 10)
pdf.cell(40, 6, 'Feature', border=1)
pdf.cell(0, 6, 'Descricao', border=1, ln=True)
pdf.set_font('Arial', '', 9)
for feature, desc in features_data:
    pdf.cell(40, 6, feature, border=1)
    pdf.cell(0, 6, desc, border=1, ln=True)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n1.3 Tratamento de Valores Faltantes', ln=True)
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5,
'- Metodo: Imputacao com media\n' +
'- Coluna afetada: margin_low (37 valores)\n' +
'- Resultado: Dataset completo com 1.500 registros')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n1.4 Normalizacao de Dados', ln=True)
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5,
'- Metodo: StandardScaler (Z-score normalization)\n' +
'- Formula: (X - media) / desvio_padrao\n' +
'- Intervalo: [-3, 3]\n' +
'- Proposito: Melhorar convergencia do modelo')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n1.5 Divisao treino/teste', ln=True)
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5,
'- Metodo: Stratified Split (mantém proporcao de classes)\n' +
'- Treino: 1.200 registros (80%)\n' +
'- Teste: 300 registros (20%)\n' +
'- Random State: 42 (reproducibilidade)')

# ===== PÁGINA 3: ARQUITETURA E TREINAMENTO =====
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*DARK_BLUE)
pdf.cell(0, 10, '2. ARQUITETURA E TREINAMENTO DA REDE NEURAL', ln=True)
pdf.set_text_color(*TEXT_COLOR)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '2.1 Arquitetura da Rede Neural', ln=True)
pdf.set_font('Arial', '', 10)

# Desenhar arquitetura simplificada
pdf.cell(0, 6, 'Input Layer (6 features)  |  64 neurons (ReLU)  |  32 neurons (ReLU)  |  16 neurons (ReLU)  |  Output (Sigmoid)', ln=True)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n2.2 Configuracao do Modelo', ln=True)
pdf.set_font('Arial', '', 10)

config_data = [
    ['Camadas ocultas', '3 (64 -> 32 -> 16 neuronios)'],
    ['Funcao de ativacao', 'ReLU (camadas ocultas), Sigmoid (saida)'],
    ['Otimizador', 'Adam'],
    ['Loss function', 'Binary Crossentropy'],
    ['Batch size', '32'],
    ['Epocas maximas', '50'],
    ['Validacao', '20% do treino'],
    ['Early stopping', 'Sim (paciencia: 20 iteracoes)']
]

pdf.set_font('Arial', 'B', 10)
pdf.cell(50, 6, 'Parametro', border=1)
pdf.cell(0, 6, 'Valor', border=1, ln=True)
pdf.set_font('Arial', '', 9)
for param, value in config_data:
    pdf.cell(50, 6, param, border=1)
    pdf.cell(0, 6, value, border=1, ln=True)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n2.3 Processo de Treinamento', ln=True)
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5,
'- Iteracoes realizadas: 30 (parou por early stopping)\n' +
'- Loss final: 0.0298\n' +
'- Tempo de treinamento: ~2-3 segundos\n' +
'- Convergencia: Rapida e suave (sem overfitting aparente)')

# ===== PÁGINA 4: RESULTADOS E ANÁLISE =====
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*DARK_BLUE)
pdf.cell(0, 10, '3. RESULTADOS E ANALISE DE PERFORMANCE', ln=True)
pdf.set_text_color(*TEXT_COLOR)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '3.1 Metricas de Performance', ln=True)

metrics_data = [
    ['Acuracia', '0.9767', '97.67%'],
    ['Precisao', '0.9754', '97.54%'],
    ['Recall (Sensibilidade)', '0.9900', '99.00%'],
    ['F1-Score', '0.9826', '98.26%'],
    ['ROC-AUC', '0.9987', '99.87%']
]

pdf.set_font('Arial', 'B', 10)
pdf.cell(60, 6, 'Metrica', border=1)
pdf.cell(40, 6, 'Valor (0-1)', border=1)
pdf.cell(0, 6, 'Percentual', border=1, ln=True)
pdf.set_font('Arial', '', 9)
for metric, value, percent in metrics_data:
    pdf.cell(60, 6, metric, border=1)
    pdf.cell(40, 6, value, border=1)
    pdf.cell(0, 6, percent, border=1, ln=True)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n3.2 Matriz de Confusao (Conjunto de Teste)', ln=True)
pdf.set_font('Arial', '', 10)

pdf.cell(50, 6, '', border=0)
pdf.cell(40, 6, 'Falsa (pred)', border=1, align='C')
pdf.cell(0, 6, 'Genuina (pred)', border=1, ln=True, align='C')

pdf.cell(50, 6, 'Falsa (real)', border=1)
pdf.cell(40, 6, '95 (TN)', border=1, align='C')
pdf.cell(0, 6, '5 (FN)', border=1, ln=True, align='C')

pdf.cell(50, 6, 'Genuina (real)', border=1)
pdf.cell(40, 6, '2 (FP)', border=1, align='C')
pdf.cell(0, 6, '198 (TP)', border=1, ln=True, align='C')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n3.3 Interpretacao dos Resultados', ln=True)
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5,
'Verdadeiros Negativos (TN): 95\n' +
'- Notas falsas corretamente identificadas como falsas\n\n' +
'Verdadeiros Positivos (TP): 198\n' +
'- Notas genuinas corretamente identificadas como genuinas\n\n' +
'Falsos Negativos (FN): 5\n' +
'- Notas falsas nao detectadas (risco de fraude)\n\n' +
'Falsos Positivos (FP): 2\n' +
'- Notas genuinas rejeitadas incorretamente (impacto comercial)')

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '\n3.4 Significado das Metricas', ln=True)
pdf.set_font('Arial', '', 9)
pdf.multi_cell(0, 4,
'Acuracia (97.67%): Percentual de previsoes corretas\n' +
'Precisao (97.54%): Das notas preditas como genuinas, quantas realmente sao\n' +
'Recall (99.00%): Das notas genuinas reais, quantas foram detectadas\n' +
'F1-Score (98.26%): Media harmonica entre precisao e recall\n' +
'ROC-AUC (0.9987): Capacidade de discriminacao entre classes (excelente > 0.9)')

# ===== PÁGINA 5: GRÁFICOS =====
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*DARK_BLUE)
pdf.cell(0, 10, '4. GRAFICOS E VISUALIZACOES', ln=True)
pdf.set_text_color(*TEXT_COLOR)

# Adicionar imagem dos gráficos
if os.path.exists('performance_analysis.png'):
    pdf.image('performance_analysis.png', x=10, y=30, w=190)
else:
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, '[Imagem nao disponivel]', ln=True)

# ===== PÁGINA 6: CONCLUSÃO =====
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(*DARK_BLUE)
pdf.cell(0, 10, '5. CONCLUSAO', ln=True)
pdf.set_text_color(*TEXT_COLOR)

pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6,
'O projeto foi desenvolvido com sucesso utilizando KNIME e Python para a implementacao de uma Rede Neural capaz de detectar notas falsas vs genuinas. Os resultados obtidos foram excelentes, com acuracia de 97.67% e ROC-AUC de 0.9987.\n\n' +

'Processo Realizado:\n' +
'1. Carregamento e exploracao do dataset fake_bills.csv (1.500 registros)\n' +
'2. Tratamento de valores faltantes (37 NaNs em margin_low)\n' +
'3. Normalizacao dos dados usando StandardScaler\n' +
'4. Divisao estratificada dos dados (80% treino, 20% teste)\n' +
'5. Construcao de uma Rede Neural com 3 camadas ocultas\n' +
'6. Treinamento do modelo com early stopping (30 iteracoes)\n' +
'7. Avaliacao completa do modelo com multiplas metricas\n' +
'8. Geracao de graficos e visualizacoes\n\n' +

'Dificuldades e Ajustes:\n' +
'- Valores faltantes: Inicialmente causaram erro. Resolvido com imputacao pela media.\n' +
'- Desbalanceamento de classes: Dataset tinha 66,7% notas genuinas. Usamos stratified split.\n' +
'- Implementacao: Comecamos com TensorFlow/Keras, mas migramos para scikit-learn por compatibilidade.\n\n' +

'Experiencia:\n' +
'O projeto proporcionou excelente aprendizado sobre todo o pipeline de machine learning, desde preparacao dos dados ate avaliacao do modelo. O uso de KNIME permitiu uma visualizacao clara do fluxo de processamento. A Rede Neural convergiu rapidamente (30 epocas) e mostrou excelente generalizacao sem sinais aparentes de overfitting. O modelo esta pronto para producao.\n\n' +

'Melhorias Futuras:\n' +
'- Testar outras arquiteturas de rede (mais camadas, neurônios diferentes)\n' +
'- Aplicar tecnicas de aumento de dados (data augmentation)\n' +
'- Implementar validacao cruzada para maior robustez\n' +
'- Fazer fine-tuning dos hiperparametros\n' +
'- Analisar feature importance para entender quais medicoes sao mais relevantes')

# Rodapé
pdf.ln(10)
pdf.set_font('Arial', 'I', 9)
pdf.set_text_color(128, 128, 128)
pdf.cell(0, 6, f'Relatorio gerado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', align='C')

# Salvar PDF
pdf.output('VitorHugoVasconcelosdeLima_ProjetoFinal.pdf')
print('✓ PDF criado com sucesso: VitorHugoVasconcelosdeLima_ProjetoFinal.pdf')
