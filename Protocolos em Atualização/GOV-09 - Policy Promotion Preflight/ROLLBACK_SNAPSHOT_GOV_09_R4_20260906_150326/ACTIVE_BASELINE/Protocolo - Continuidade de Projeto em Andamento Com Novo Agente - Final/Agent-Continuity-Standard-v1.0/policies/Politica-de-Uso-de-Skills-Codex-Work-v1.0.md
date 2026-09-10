# Política de Uso de Skills — Codex + Work
## Versão 1.0

**Status:** Documento de referência operacional  
**Escopo:** Projetos de software, pesquisa, arquitetura, experimentação, governança, documentação, análise e operação  
**Aplicação:** Neutra e transversal; não vinculada a nenhum agente, projeto, linguagem ou repositório específico  
**Objetivo:** Dar liberdade operacional para que agentes escolham, de forma autônoma e responsável, quais skills utilizar, quando utilizá-las, como combiná-las e quando evitá-las.

---

# 1. Objetivo

Este documento estabelece uma política geral para uso de **skills disponíveis no ecossistema Codex + Work**.

A intenção não é obrigar o uso de skills em todas as tarefas. Pelo contrário: a regra central é utilizar uma skill **somente quando ela aumentar de forma material a qualidade, a rastreabilidade, a eficiência, a segurança, a clareza ou a consistência do trabalho**.

Os agentes estão autorizados a:

- selecionar autonomamente a skill mais adequada para a tarefa;
- não utilizar nenhuma skill quando a capacidade nativa do ambiente for suficiente;
- combinar skills quando houver ganho real;
- substituir uma skill inicialmente considerada por outra mais adequada;
- interromper o uso de uma skill quando ela deixar de agregar valor;
- utilizar ferramentas nativas do Codex ou Work sem skill intermediária quando isso for mais simples;
- justificar decisões com base em custo, complexidade, risco, rastreabilidade e adequação técnica.

A autonomia concedida por esta política **não substitui requisitos de segurança, governança, permissões, gates, políticas do projeto ou limitações da plataforma**.

---

# 2. Princípio fundamental

> **Use a menor capacidade suficiente para resolver corretamente a tarefa.**

Uma skill não deve ser acionada apenas porque existe.

O uso adequado deve seguir esta ordem de raciocínio:

1. A tarefa pode ser resolvida diretamente com as capacidades nativas?
2. Uma skill adiciona estrutura, evidência, rastreabilidade ou produtividade relevante?
3. Existe uma skill claramente alinhada ao problema?
4. O custo de coordenação da skill é menor que o benefício esperado?
5. Existe risco de duplicação ou sobreposição com outra skill?
6. O resultado produzido pela skill será efetivamente usado?
7. A skill respeita as regras de disponibilidade e acionamento da plataforma?

Se a resposta prática for “não”, a skill deve ser evitada.

---

# 3. Separação conceitual: Codex, Work e Skills

## 3.1 Codex

Codex deve ser entendido principalmente como ambiente especializado em execução de engenharia de software.

Atividades típicas:

- leitura e inspeção de repositório;
- implementação;
- correção de bugs;
- refatoração;
- testes;
- integração;
- análise de dependências;
- investigação de falhas;
- revisão de código;
- mudanças em arquivos;
- validação de build;
- execução de comandos;
- trabalho com Git;
- análise de regressão.

Não é necessário procurar uma “skill de programação” para cada uma dessas atividades.

Quando a capacidade nativa do Codex for suficiente, ela deve ser usada diretamente.

---

## 3.2 Work

Work é particularmente adequado para atividades persistentes, estruturadas e orientadas a artefatos ou análise.

Exemplos:

- pesquisa;
- arquitetura;
- planejamento;
- documentação;
- criação de relatórios;
- planilhas;
- apresentações;
- análise estratégica;
- consolidação de evidências;
- síntese de decisões;
- acompanhamento de projetos.

---

## 3.3 Skills

Skills são procedimentos especializados reutilizáveis.

Elas podem fornecer:

- estrutura;
- templates;
- metodologia;
- instruções especializadas;
- artefatos pré-formatados;
- fluxos de trabalho;
- integração com plugins;
- padronização de saídas.

Uma skill deve ser tratada como **instrumento operacional**, não como autoridade final.

---

# 4. Política de autonomia

Os agentes têm liberdade para escolher a skill apropriada, desde que observem os seguintes princípios.

## 4.1 Adequação

A skill escolhida deve corresponder diretamente ao problema.

## 4.2 Economia

Não utilizar duas ou mais skills quando uma única capacidade resolve a tarefa satisfatoriamente.

## 4.3 Rastreabilidade

Para decisões importantes, preferir processos que permitam identificar:

- hipótese;
- evidência;
- análise;
- decisão;
- riscos;
- limitações;
- resultado.

## 4.4 Continuidade

O uso de uma skill não deve apagar, contradizer ou substituir silenciosamente decisões já estabelecidas no projeto.

## 4.5 Independência analítica

Templates e skills não devem induzir decisões automáticas.

A decisão final deve continuar baseada em:

- evidência;
- requisitos;
- riscos;
- trade-offs;
- contexto real do projeto.

## 4.6 Escalonamento proporcional

Skills mais complexas devem ser usadas apenas quando a tarefa justificar.

Exemplo:

```text
Pergunta simples
    ↓
Resposta direta

Problema técnico localizado
    ↓
Codex

Decisão arquitetural relevante
    ↓
System Design / Strategy Memorandum

Pesquisa extensa ou controvertida
    ↓
Deep Research

Experimento formal
    ↓
Experiment Analysis
```

---

# 5. Classificação geral das skills

As skills disponíveis podem ser agrupadas em sete famílias:

1. **Arquitetura e estratégia**
2. **Pesquisa e inteligência**
3. **Experimentação e análise**
4. **Gestão e governança**
5. **Métricas e finanças**
6. **Documentação e comunicação**
7. **Artefatos e extensibilidade**

---

# 6. Skills de arquitetura e estratégia

## 6.1 System Design

**Categoria:** Arquitetura  
**Prioridade sugerida:** Muito alta

### Finalidade

Produzir documentação estruturada de arquitetura de sistemas, incluindo:

- requisitos;
- componentes;
- responsabilidades;
- interfaces;
- APIs;
- fluxos de dados;
- dependências;
- trade-offs;
- escalabilidade;
- disponibilidade;
- segurança;
- operação;
- observabilidade;
- recuperação;
- riscos.

### Quando usar

Utilizar quando houver:

- criação de subsistema;
- mudança arquitetural;
- integração complexa;
- alteração de persistência;
- concorrência;
- processamento distribuído;
- mudanças em contratos;
- decisões difíceis de reverter;
- necessidade de documentar arquitetura antes da implementação.

### Quando não usar

Evitar para:

- bug localizado;
- alteração cosmética;
- renomeação;
- refatoração simples;
- pequeno endpoint sem impacto arquitetural;
- ajuste trivial de configuração.

### Benefícios

- reduz improvisação;
- explicita trade-offs;
- facilita revisão;
- melhora continuidade entre sessões;
- fornece referência para implementação;
- reduz divergências entre agentes.

### Riscos de uso excessivo

- documentação desnecessária;
- arquitetura superdimensionada;
- atraso em tarefas simples;
- “design por template” sem necessidade real.

---

## 6.2 Strategy Memorandum

**Categoria:** Estratégia e decisão  
**Prioridade sugerida:** Muito alta

### Finalidade

Estruturar decisões importantes por meio de:

- contexto;
- problema;
- alternativas;
- racional;
- riscos;
- consequências;
- milestones;
- recomendação.

### Quando usar

Ideal para:

- escolher entre arquiteturas;
- escolher tecnologia;
- decidir build vs. buy;
- priorizar roadmap;
- decidir migração;
- avaliar opções de implementação;
- decidir entre alternativas com custos relevantes.

### Quando não usar

Evitar quando:

- existe uma única solução óbvia;
- a decisão é trivial;
- o custo de reversão é baixo;
- uma explicação curta é suficiente.

### Benefícios

- força comparação explícita;
- reduz decisões intuitivas;
- registra racional;
- melhora governança;
- facilita auditoria futura.

### Riscos

- burocratização;
- excesso de formalismo;
- falsa impressão de precisão em decisões com pouca evidência.

---

## 6.3 Design Report

**Categoria:** Design / UX / avaliação  
**Prioridade sugerida:** Alta

### Finalidade

Produzir relatórios estruturados contendo:

- resumo executivo;
- achados;
- evidências;
- implicações;
- recomendações;
- anexos.

### Quando usar

Adequado para:

- auditoria UI/UX;
- análise de Design System;
- revisão de experiência operacional;
- avaliação de interface;
- comparação de padrões visuais;
- diagnóstico de usabilidade.

### Quando não usar

Evitar para pequenos ajustes visuais já claramente definidos.

### Benefícios

- transforma observações em findings rastreáveis;
- diferencia problema de recomendação;
- melhora consistência visual;
- facilita priorização.

---

# 7. Skills de pesquisa e inteligência

## 7.1 Deep Research

**Categoria:** Pesquisa aprofundada  
**Prioridade sugerida:** Muito alta, porém seletiva

### Finalidade

Executar pesquisa extensa e fundamentada em múltiplas fontes, produzindo análise baseada em evidências e citações.

### Quando usar

Apenas quando houver necessidade real de pesquisa aprofundada, por exemplo:

- estado da arte;
- tecnologias emergentes;
- comparação ampla de soluções;
- investigação científica;
- pesquisa regulatória;
- análise de mercado;
- análise de literatura;
- validação externa complexa;
- temas em que várias fontes precisam ser conciliadas.

### Regra operacional importante

Esta skill possui condições próprias de acionamento na plataforma e deve ser utilizada somente quando explicitamente disponibilizada/selecionada para Deep Research ou quando o contexto permitir seu uso conforme as regras vigentes.

### Quando não usar

Não utilizar para:

- consulta simples;
- documentação oficial fácil de localizar;
- pergunta factual direta;
- investigação que pode ser resolvida por poucas fontes.

### Benefícios

- maior profundidade;
- melhor cobertura;
- múltiplas evidências;
- citações;
- redução de viés de fonte única.

### Riscos

- custo elevado;
- excesso de informação;
- demora cognitiva;
- pesquisa desproporcional ao problema.

---

## 7.2 Market Trends Report

**Categoria:** Inteligência de mercado  
**Prioridade sugerida:** Média

### Finalidade

Analisar:

- tendências;
- sinais de mercado;
- mudanças de indústria;
- evidências;
- implicações;
- possíveis respostas estratégicas.

### Quando usar

Adequado para:

- mercados tecnológicos;
- IA;
- fintech;
- criptomoedas;
- plataformas;
- concorrência;
- comportamento setorial.

### Quando não usar

Evitar quando a tarefa é puramente técnica e interna.

### Benefícios

- contextualização externa;
- identificação de tendências;
- suporte a decisões estratégicas.

---

# 8. Skills de experimentação e análise

## 8.1 Experiment Analysis

**Categoria:** Experimentação  
**Prioridade sugerida:** Muito alta

### Finalidade

Formalizar análise de experimentos por meio de:

- hipótese;
- metodologia;
- variáveis;
- resultados;
- interpretação;
- limitações;
- conclusão;
- próximos passos.

### Quando usar

Excelente para:

- backtesting;
- benchmarking;
- A/B testing;
- ablation tests;
- testes de performance;
- experimentos de ML;
- avaliação de estratégias;
- comparação entre algoritmos;
- testes de parâmetros;
- validação estatística;
- experimentos de UX.

### Quando não usar

Evitar quando não existe experimento.

Uma simples execução de teste unitário não precisa virar Experiment Analysis.

### Benefícios

- reduz cherry-picking;
- força hipótese prévia;
- explicita limitações;
- melhora reprodutibilidade;
- diferencia resultado de interpretação.

### Riscos

- formalização artificial de tarefas triviais;
- excesso de documentação;
- aparência científica sem desenho experimental adequado.

---

# 9. Skills de gestão e governança

## 9.1 Project Tracker

**Categoria:** Gestão de projeto  
**Prioridade sugerida:** Muito alta

### Finalidade

Organizar:

- workstreams;
- tarefas;
- responsáveis;
- status;
- prioridades;
- datas;
- milestones;
- dependências;
- cronogramas;
- Gantt.

### Quando usar

Indicado para projetos com:

- múltiplas sprints;
- várias frentes;
- dependências;
- entregas sequenciais;
- diversos agentes;
- necessidade de acompanhamento persistente.

### Quando não usar

Evitar para tarefa única ou projeto pequeno sem dependências.

### Benefícios

- visão consolidada;
- redução de perda de contexto;
- acompanhamento objetivo;
- identificação de bloqueios.

### Riscos

- tracker desatualizado;
- duplicação de fontes de verdade;
- microgestão.

---

## 9.2 Operating Review

**Categoria:** Governança operacional  
**Prioridade sugerida:** Alta

### Finalidade

Criar revisões periódicas com:

- scorecards;
- status;
- riscos;
- decisões;
- ações;
- pendências.

### Quando usar

Ideal para:

- fechamento de sprint;
- revisão semanal;
- checkpoints operacionais;
- review de release;
- revisão de incidentes recorrentes.

### Quando não usar

Evitar para tarefas sem ciclo operacional.

### Benefícios

- padroniza checkpoints;
- explicita riscos;
- captura decisões;
- facilita continuidade.

---

## 9.3 Operating Calendar

**Categoria:** Planejamento temporal  
**Prioridade sugerida:** Média

### Finalidade

Organizar:

- milestones;
- lançamentos;
- deadlines;
- eventos;
- atividades recorrentes;
- calendário operacional.

### Quando usar

Projetos com calendário relevante ou múltiplas entregas temporais.

### Quando não usar

Projetos cujo progresso é definido por dependências técnicas, e não por datas.

### Benefícios

- visualização temporal;
- prevenção de conflitos;
- organização de releases.

---

## 9.4 Project Kickoff

**Categoria:** Inicialização de projeto  
**Prioridade sugerida:** Alta

### Finalidade

Definir:

- objetivos;
- escopo;
- papéis;
- milestones;
- riscos;
- modelo de trabalho.

### Quando usar

- novo projeto;
- nova fase;
- nova sprint de grande porte;
- novo subsistema;
- equipe/agentes novos.

### Quando não usar

Evitar para microtarefas dentro de um contexto já estabelecido.

### Benefícios

- reduz ambiguidades iniciais;
- alinha expectativas;
- explicita escopo.

---

## 9.5 Team Alignment

**Categoria:** Coordenação  
**Prioridade sugerida:** Média

### Finalidade

Consolidar:

- contexto;
- objetivos;
- prioridades;
- decisões;
- ações.

### Quando usar

Quando múltiplos participantes ou agentes precisam operar sob o mesmo estado de decisão.

### Quando não usar

Quando existe apenas um executor e o contexto está claro.

### Benefícios

- reduz divergência;
- cria linguagem comum;
- consolida prioridades.

---

## 9.6 Business Review

**Categoria:** Revisão executiva  
**Prioridade sugerida:** Média

### Finalidade

Revisar:

- KPIs;
- desempenho;
- segmentos;
- prioridades;
- decisões;
- outlook.

### Quando usar

Mais apropriado para produtos ou operações maduras.

### Quando não usar

Evitar em fases iniciais puramente técnicas.

### Benefícios

- visão executiva;
- conexão entre tecnologia e resultado.

---

# 10. Skills de métricas, analytics e finanças

## 10.1 Analytics Dashboard

**Categoria:** Métricas  
**Prioridade sugerida:** Alta

### Finalidade

Construir dashboards de KPIs e indicadores.

Embora o template possua exemplos de aquisição, engajamento, retenção, receita e conversão, ele pode ser adaptado a outros tipos de métricas quando apropriado.

### Exemplos

Software:

- cobertura de testes;
- bugs;
- incidentes;
- latência;
- throughput;
- deploy frequency.

Trading:

- PnL;
- drawdown;
- Sharpe;
- Sortino;
- win rate;
- expectancy;
- exposição;
- turnover;
- regime.

ML:

- accuracy;
- precision;
- recall;
- F1;
- calibration;
- drift.

### Benefícios

- comunicação visual;
- detecção rápida de deterioração;
- acompanhamento contínuo.

### Riscos

- escolher KPI errado;
- dashboard sem ação associada;
- excesso de métricas.

---

## 10.2 Financial Budget

**Categoria:** Planejamento financeiro  
**Prioridade sugerida:** Baixa a média

### Finalidade

Modelar:

- orçamento;
- actuals;
- forecast;
- variâncias;
- runway;
- departamentos.

### Quando usar

- produto comercial;
- operação empresarial;
- planejamento de custos;
- infraestrutura paga;
- orçamento de equipe.

### Quando não usar

Projeto puramente técnico sem componente financeiro relevante.

---

## 10.3 Three-Statement Forecast

**Categoria:** Modelagem financeira  
**Prioridade sugerida:** Baixa

### Finalidade

Integrar:

- demonstração de resultados;
- balanço patrimonial;
- fluxo de caixa.

### Quando usar

Somente em contexto empresarial/financeiro que realmente exija modelagem contábil integrada.

### Benefício

Avaliação econômico-financeira completa.

---

## 10.4 Investment Committee Memo

**Categoria:** Investimentos  
**Prioridade sugerida:** Baixa a média

### Finalidade

Estruturar:

- tese;
- análise;
- riscos;
- números;
- recomendação.

### Quando usar

Avaliação formal de investimento ou capital allocation.

### Quando não usar

Não utilizar como substituto de análise quantitativa ou due diligence.

---

## 10.5 Sales Pipeline

**Categoria:** Comercial  
**Prioridade sugerida:** Baixa

### Finalidade

Gerenciar:

- oportunidades;
- estágio;
- responsável;
- tamanho;
- probabilidade;
- forecast;
- próximos passos.

### Quando usar

Somente quando houver atividade comercial real.

---

# 11. Skills de documentação e comunicação

## 11.1 Legal Memorandum

**Categoria:** Jurídico  
**Prioridade sugerida:** Situacional

### Finalidade

Estruturar:

- issue;
- brief answer;
- fatos;
- análise;
- conclusão.

### Quando usar

- análise regulatória;
- contratos;
- políticas;
- compliance;
- questões legais estruturadas.

### Observação

Não substitui advogado ou parecer jurídico profissional quando exigido.

---

## 11.2 Minimal Letterhead

**Categoria:** Comunicação corporativa  
**Prioridade sugerida:** Situacional

### Finalidade

Produzir cartas formais em layout profissional.

### Uso adequado

Comunicação empresarial, institucional ou administrativa.

---

# 12. Skills de apresentação

## 12.1 Simple Dark Mode

**Categoria:** Apresentação  
**Prioridade sugerida:** Situacional

### Finalidade

Criar apresentações modernas em tema escuro.

### Quando usar

- apresentação técnica;
- produto;
- dashboard;
- review;
- demonstração visual.

---

## 12.2 Simple Light Mode

**Categoria:** Apresentação  
**Prioridade sugerida:** Situacional

### Finalidade

Criar apresentações claras e minimalistas.

### Quando usar

- ambiente corporativo;
- relatórios;
- documentação executiva;
- reuniões.

---

# 13. Skills de artefatos

Estas skills funcionam como roteadores para capacidades especializadas de criação de artefatos.

## 13.1 @document

**Finalidade:** criação e edição de documentos estruturados.

### Adequado para

- especificações;
- relatórios;
- manuais;
- arquitetura;
- ADRs;
- propostas;
- documentação formal.

### Regra

Deve ser utilizada de acordo com as condições de acionamento da plataforma, especialmente quando explicitamente selecionada.

---

## 13.2 @spreadsheet

**Finalidade:** criação e edição de planilhas.

### Adequado para

- trackers;
- métricas;
- modelos;
- experimentos;
- forecasts;
- planejamento;
- datasets tabulares.

---

## 13.3 @presentation

**Finalidade:** criação e edição de apresentações.

### Adequado para

- reviews;
- roadmap;
- kickoff;
- relatórios executivos;
- apresentações técnicas.

---

## 13.4 @pdf

**Finalidade:** produção e manipulação de PDF.

### Adequado para

- versão final de relatório;
- documento para distribuição;
- documentação imutável;
- publicação formal.

---

# 14. Skills de extensibilidade

## 14.1 Template Creator

**Categoria:** Padronização / extensibilidade  
**Prioridade sugerida:** Muito alta

### Finalidade

Transformar materiais existentes em templates ou skills reutilizáveis.

### Quando usar

Quando uma estrutura começa a se repetir.

Exemplos:

- especificação de sprint;
- relatório de auditoria;
- ADR;
- protocolo de backtest;
- review de release;
- checklist de segurança;
- envelope de tarefa;
- relatório pós-incidente;
- política de governança.

### Regra prática

> Se o mesmo tipo de artefato ou procedimento foi recriado manualmente três ou mais vezes, considerar Template Creator.

### Benefícios

- consistência;
- redução de prompts extensos;
- menor retrabalho;
- preservação da metodologia;
- escalabilidade operacional.

### Riscos

- cristalizar processos ruins;
- criar templates cedo demais;
- impedir evolução natural do processo.

---

## 14.2 Plugin Management

**Categoria:** Extensibilidade  
**Prioridade sugerida:** Alta quando necessária

### Finalidade

Descobrir e gerenciar:

- plugins;
- permissões;
- dependências;
- conexões;
- integrações externas.

### Quando usar

Quando uma tarefa exige dados ou ações que as capacidades atuais não oferecem.

### Quando não usar

Não procurar plugin apenas por curiosidade quando o ambiente atual já resolve a tarefa.

### Benefícios

- expansão controlada de capacidade;
- descoberta de integrações;
- inspeção de permissões.

### Riscos

- dependências desnecessárias;
- superfície adicional de segurança;
- complexidade operacional.

---

# 15. Matriz tarefa → skill recomendada

| Tipo de tarefa | Skill principal | Alternativa / complemento |
|---|---|---|
| Nova arquitetura | System Design | Strategy Memorandum |
| Decisão entre alternativas | Strategy Memorandum | System Design |
| Pesquisa extensa | Deep Research | Market Trends Report |
| Pesquisa de tendência | Market Trends Report | Deep Research |
| Backtest formal | Experiment Analysis | Analytics Dashboard |
| Benchmark | Experiment Analysis | @spreadsheet |
| Auditoria UI/UX | Design Report | System Design |
| Criar Design System | Design Report | System Design |
| Planejar sprint | Project Tracker | Project Kickoff |
| Iniciar projeto | Project Kickoff | System Design |
| Fechar sprint | Operating Review | Project Tracker |
| Acompanhar KPIs | Analytics Dashboard | Operating Review |
| Cronograma | Operating Calendar | Project Tracker |
| Alinhar múltiplos participantes | Team Alignment | Project Kickoff |
| Criar padrão repetível | Template Creator | @document |
| Encontrar integração externa | Plugin Management | — |
| Relatório formal | @document | @pdf |
| Planilha de acompanhamento | @spreadsheet | Project Tracker |
| Apresentação executiva | @presentation | Business Review |
| Apresentação técnica | Simple Dark Mode / Light Mode | @presentation |
| Avaliação financeira | Financial Budget | Three-Statement Forecast |
| Avaliação de investimento | Investment Committee Memo | Experiment Analysis |
| Análise regulatória | Legal Memorandum | Deep Research |

---

# 16. Heurística de decisão

Utilizar o seguinte fluxo mental:

```text
INÍCIO
  │
  ├─ A tarefa é principalmente implementação?
  │      └─ SIM → usar Codex diretamente
  │
  ├─ É uma decisão arquitetural?
  │      └─ SIM → System Design
  │
  ├─ Existem várias alternativas relevantes?
  │      └─ SIM → Strategy Memorandum
  │
  ├─ Depende de pesquisa externa extensa?
  │      └─ SIM → Deep Research
  │
  ├─ Existe hipótese experimental?
  │      └─ SIM → Experiment Analysis
  │
  ├─ É avaliação de UI/UX/design?
  │      └─ SIM → Design Report
  │
  ├─ É acompanhamento de tarefas?
  │      └─ SIM → Project Tracker
  │
  ├─ É revisão periódica?
  │      └─ SIM → Operating Review
  │
  ├─ O resultado precisa virar dashboard?
  │      └─ SIM → Analytics Dashboard
  │
  ├─ O procedimento se repete?
  │      └─ SIM → Template Creator
  │
  ├─ Falta integração/capacidade?
  │      └─ SIM → Plugin Management
  │
  └─ Nenhuma skill agrega valor
         └─ executar diretamente
```

---

# 17. Combinação de skills

Skills podem ser combinadas, mas a combinação deve possuir propósito explícito.

## 17.1 Pesquisa → decisão → arquitetura

```text
Deep Research
      ↓
Strategy Memorandum
      ↓
System Design
      ↓
Codex
```

Uso adequado quando uma mudança arquitetural depende de conhecimento externo.

---

## 17.2 Arquitetura → implementação → review

```text
System Design
      ↓
Codex
      ↓
testes
      ↓
Operating Review
```

---

## 17.3 Experimento quantitativo

```text
Hipótese
   ↓
Experiment Analysis
   ↓
Codex / execução
   ↓
@spreadsheet
   ↓
Analytics Dashboard
   ↓
Experiment Analysis final
```

---

## 17.4 UI/UX

```text
Referências / pesquisa
      ↓
Design Report
      ↓
System Design
      ↓
Codex
      ↓
Review visual
```

---

## 17.5 Novo projeto

```text
Project Kickoff
      ↓
Strategy Memorandum
      ↓
System Design
      ↓
Project Tracker
      ↓
Codex
```

---

# 18. Regra de não sobreposição

Evitar combinações que gerem o mesmo tipo de trabalho.

Exemplos desaconselhados:

```text
System Design
+
Strategy Memorandum
+
Design Report
+
Business Review
```

para uma alteração simples.

Outro exemplo:

```text
Project Tracker
+
Operating Calendar
+
Team Alignment
```

quando um tracker simples é suficiente.

A pergunta deve ser:

> “Cada skill desta combinação possui responsabilidade distinta?”

Se não houver resposta clara, simplificar.

---

# 19. Fluxo recomendado de engenharia

Um fluxo completo possível é:

```text
PROBLEMA
   ↓
Pesquisa necessária?
   ├── não
   └── sim → Deep Research
               ↓
Decisão relevante?
   ├── não
   └── sim → Strategy Memorandum
               ↓
Arquitetura necessária?
   ├── não
   └── sim → System Design
               ↓
IMPLEMENTAÇÃO
   ↓
Codex
   ├── código
   ├── testes
   ├── integração
   ├── revisão
   └── validação
               ↓
Experimento?
   └── Experiment Analysis
               ↓
Review operacional?
   └── Operating Review
               ↓
Documentação
   ├── @document
   ├── @spreadsheet
   ├── @presentation
   └── @pdf
               ↓
PROCESSO RECORRENTE?
   └── Template Creator
```

Este é um fluxo de referência, não uma sequência obrigatória.

---

# 20. Anti-padrões

## 20.1 Skill por padrão

Errado:

> “Existe uma skill, portanto devemos usá-la.”

Correto:

> “Existe ganho material ao usar esta skill?”

---

## 20.2 Overengineering documental

Produzir:

- arquitetura;
- estratégia;
- relatório;
- apresentação;
- tracker;
- dashboard;

para uma alteração de cinco linhas de código é um uso inadequado.

---

## 20.3 Delegação de decisão

A skill não deve decidir automaticamente uma questão crítica.

Ela estrutura o raciocínio.

---

## 20.4 Template como verdade

Templates podem ficar obsoletos.

O agente deve validar se o template ainda corresponde:

- ao projeto;
- à arquitetura;
- à governança;
- à realidade operacional.

---

## 20.5 Duplicação de fonte de verdade

Se existe um tracker oficial, não criar outro sem necessidade.

Se existe uma especificação oficial, não criar uma segunda especificação concorrente.

---

## 20.6 Pesquisa sem hipótese

Pesquisa extensa sem pergunta clara tende a gerar volume, não conhecimento.

---

## 20.7 Dashboard sem decisão

Uma métrica só é útil se puder influenciar uma decisão ou detectar um estado relevante.

---

# 21. Checklist antes de usar uma skill

Antes de selecionar uma skill, responder mentalmente:

- [ ] Qual problema concreto preciso resolver?
- [ ] A capacidade nativa já resolve?
- [ ] Esta skill adiciona valor material?
- [ ] Ela corresponde diretamente à tarefa?
- [ ] Há outra skill mais simples?
- [ ] Estou duplicando trabalho existente?
- [ ] O resultado será utilizado?
- [ ] Há regras específicas para acionamento?
- [ ] O custo/complexidade é proporcional?
- [ ] A skill preservará decisões oficiais do projeto?

Se várias respostas forem negativas, não usar a skill.

---

# 22. Checklist após usar uma skill

Após execução:

- [ ] O resultado responde à necessidade original?
- [ ] Evidências e hipóteses estão separadas?
- [ ] Limitações foram registradas?
- [ ] A saída contradiz alguma decisão oficial?
- [ ] Existe duplicação de documentação?
- [ ] É necessário atualizar tracker ou documentação?
- [ ] Alguma decisão precisa de aprovação humana?
- [ ] O artefato deve se tornar template?
- [ ] A skill realmente agregou valor?
- [ ] Há lições para usos futuros?

---

# 23. Política para tarefas críticas

Para atividades de alto impacto, como:

- segurança;
- dinheiro real;
- produção;
- dados irreversíveis;
- migração;
- autenticação;
- autorização;
- persistência;
- concorrência;
- disponibilidade;
- recuperação;
- compliance;

a skill pode auxiliar, porém **não elimina gates, validações, revisão independente ou autorização exigida pelo projeto**.

Em tarefas críticas, preferir:

```text
evidência
→ análise
→ decisão explícita
→ implementação
→ teste
→ revisão
→ autorização
```

---

# 24. Prioridades sugeridas

## Tier A — uso estratégico frequente

- System Design
- Experiment Analysis
- Deep Research
- Strategy Memorandum
- Project Tracker
- Template Creator

## Tier B — uso recorrente

- Design Report
- Operating Review
- Analytics Dashboard
- Plugin Management
- Project Kickoff

## Tier C — situacional

- Operating Calendar
- Team Alignment
- Business Review
- Market Trends Report
- @document
- @spreadsheet
- @presentation
- @pdf

## Tier D — especializado

- Financial Budget
- Three-Statement Forecast
- Investment Committee Memo
- Sales Pipeline
- Legal Memorandum
- Minimal Letterhead
- Simple Dark Mode
- Simple Light Mode

A classificação não representa importância absoluta. Uma skill Tier D pode ser a melhor ferramenta para uma tarefa específica.

---

# 25. Regra de seleção mínima

Sempre preferir:

```text
1 skill adequada
```

em vez de:

```text
3 skills parcialmente adequadas
```

E preferir:

```text
capacidade nativa
```

quando:

```text
skill = burocracia sem ganho
```

---

# 26. Escalonamento

Um agente pode escalar progressivamente:

### Nível 0 — Direto

Capacidade nativa.

### Nível 1 — Estrutura leve

Uma skill específica.

### Nível 2 — Fluxo composto

Duas ou três skills com funções distintas.

### Nível 3 — Pesquisa / decisão complexa

Deep Research + Strategy Memorandum + System Design.

O escalonamento deve ser motivado pela complexidade do problema, não pelo tamanho do projeto.

---

# 27. Critério para criação de nova skill

Considerar criar uma nova skill quando:

- o processo se repete;
- existem regras estáveis;
- há estrutura previsível;
- erros recorrentes seriam evitados;
- o prompt é reescrito frequentemente;
- múltiplos agentes precisam seguir o mesmo método;
- existe benefício real de padronização.

Não criar uma nova skill quando:

- processo ainda está evoluindo rapidamente;
- existem poucas ocorrências;
- regras não estão estabilizadas;
- uma skill existente já atende bem.

---

# 28. Modelo recomendado para skills personalizadas

Uma skill personalizada deve preferencialmente declarar:

```text
NOME
OBJETIVO
ESCOPO
ENTRADAS
PRÉ-CONDIÇÕES
PROCESSO
GATES
SAÍDAS
CRITÉRIOS DE PASS/FAIL
LIMITAÇÕES
ANTI-PADRÕES
QUANDO NÃO USAR
```

Isso evita skills vagas ou excessivamente genéricas.

---

# 29. Autoridade e responsabilidade

A utilização de uma skill não transfere autoridade decisória.

A responsabilidade permanece com:

1. requisitos oficiais do projeto;
2. políticas e governança;
3. evidências observadas;
4. critérios de aceitação;
5. autorização humana quando necessária.

A skill é um meio para melhorar execução e raciocínio.

---

# 30. Política oficial de liberdade operacional

Fica estabelecido que os agentes podem selecionar autonomamente skills disponíveis no ambiente, desde que:

1. a escolha seja tecnicamente justificável;
2. a skill seja proporcional à tarefa;
3. não haja violação das regras de acionamento da plataforma;
4. não sejam ignoradas decisões oficiais;
5. o uso não introduza complexidade desnecessária;
6. decisões críticas não sejam delegadas cegamente a templates;
7. haja preferência pela solução mais simples que mantenha qualidade;
8. skills de pesquisa sejam usadas quando a evidência externa realmente importar;
9. skills de arquitetura sejam usadas quando existirem consequências arquiteturais reais;
10. skills de gestão sejam usadas quando houver necessidade de acompanhamento persistente;
11. skills de artefatos sejam utilizadas quando o entregável justificar;
12. processos repetitivos possam ser candidatos a Template Creator;
13. capacidades nativas de Codex e Work permaneçam válidas quando forem suficientes.

---

# 31. Princípio final

A política pode ser resumida em:

```text
NÃO USE MAIS FERRAMENTA.
USE A FERRAMENTA CERTA.

NÃO CRIE MAIS PROCESSO.
CRIE O PROCESSO NECESSÁRIO.

NÃO PRODUZA MAIS DOCUMENTAÇÃO.
PRODUZA A DOCUMENTAÇÃO QUE PRESERVA DECISÃO E CONTINUIDADE.

NÃO DELEGUE RACIOCÍNIO À SKILL.
USE A SKILL PARA ESTRUTURAR RACIOCÍNIO MELHOR.
```

A skill ideal é aquela que melhora o resultado sem se tornar o centro do trabalho.

---

# 32. Resumo operacional

```text
IMPLEMENTAR / TESTAR / REFATORAR
→ Codex

PESQUISAR PROFUNDAMENTE
→ Deep Research

DECIDIR ENTRE ALTERNATIVAS
→ Strategy Memorandum

PROJETAR ARQUITETURA
→ System Design

VALIDAR EXPERIMENTO
→ Experiment Analysis

AUDITAR DESIGN / UX
→ Design Report

CONTROLAR EXECUÇÃO
→ Project Tracker

REVISAR OPERAÇÃO
→ Operating Review

ACOMPANHAR KPIs
→ Analytics Dashboard

PADRONIZAR PROCESSO REPETIDO
→ Template Creator

AMPLIAR CAPACIDADE
→ Plugin Management

CRIAR ARTEFATO
→ @document / @spreadsheet / @presentation / @pdf
```

---

# 33. Nota de manutenção

O catálogo de skills, plugins e capacidades da plataforma pode evoluir.

Este documento deve ser revisado quando ocorrer qualquer uma das seguintes condições:

- nova skill relevante disponível;
- mudança nas regras de acionamento;
- mudança no fluxo Codex/Work;
- criação de skills personalizadas;
- alteração de governança;
- identificação de anti-padrão recorrente;
- mudança significativa na arquitetura operacional dos projetos.

**Versão:** 1.0  
**Próxima revisão:** sob mudança material do ecossistema ou da política operacional.
