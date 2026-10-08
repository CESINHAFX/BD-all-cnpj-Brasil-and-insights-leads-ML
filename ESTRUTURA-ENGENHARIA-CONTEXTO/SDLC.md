# SDLC - Software Development Life Cycle

## Visão Geral

Este repositório implementa um guia interativo completo do ciclo de vida de desenvolvimento de software (SDLC) integrado com engenharia de contexto para GitHub Copilot.

## Estrutura do SDLC

### 1. Fases Sequenciais do Ciclo SDLC (Fluxo Principal)

Esta sequência representa o fluxo lógico de desenvolvimento, onde a saída de uma fase alimenta a próxima.

#### Etapa 1: Requisitos e Análise

Esta fase define o escopo do problema, as necessidades do cliente e as bases técnicas do projeto.

| Sub-etapa | Descrição do Processo | Resultado Necessário para o Pipeline | Expectativa do Cliente |
|-----------|----------------------|-------------------------------------|------------------------|
| 1. Coleta e Análise de Requisitos | Entendimento das necessidades do cliente e dos usuários finais, definindo o que o software deve fazer. | URS (User Requirement Specification): Documento formal que lista as funcionalidades desejadas pelos stakeholders. | Define o Critério de Sucesso, o propósito da aplicação, e a lista de funcionalidades |
| 2. Especificação do Software (SRS) | Documentação detalhada dos requisitos. | SRS (Software Requirement Specification): Documento que detalha a especificação do sistema e o como ele se comporta. | O que o sistema faz? Como ele se comporta? Define a lógica de negócios e regras de validação |
| 3. Planejamento do Protótipo | Testar ideias básicas de design e estabelecer o ambiente técnico e padrões de qualidade | Documento de Escopo do Protótipo/Design | Compatibilidade de linguagem e ambiente; Requisitos não funcionais |

##### 3.1 Detalhamento do Escopo Técnico e Qualidade da Base

| Aspecto | O que é Necessário no Protótipo / Base | Padrões de Qualidade |
|---------|----------------------------------------|---------------------|
| Estrutura Base / Layout | Escolher um repositório base que tenha estrutura completa e bem definida | Garantir que o código base utilize padrões universais de codificação (ex: PEP 8 em Python; ESLint e TypeScript em JS/Node.js) |
| Compatibilidade | Definir a linguagem e a versão mínima do ambiente de execução | Planejar Estratégias de Contingência e o uso de Polyfills e Transpiladores |
| Dependências | Listar bibliotecas obrigatórias | Definir se as dependências têm suporte oficial ou se exigem build manual |
| Requisitos Não Funcionais | Definir segurança e escalabilidade | Implementar boas práticas de segurança e modelagem de dados |

#### Etapa 2: Design e Arquitetura

Nesta fase, o arquiteto de sistemas projeta a estrutura da aplicação.

| Sub-etapa | Descrição do Processo | Produtos Gerados | Manutenção Pré-Software |
|-----------|----------------------|------------------|-------------------------|
| 1. Design de Arquitetura | Criação do blueprint do sistema, definindo a Arquitetura de Software (ex: SOA - Service-Oriented Architecture) | Software Architecture Document e diagramas (ex: UML, Diagramas de Classe) | Design para Robustez e Segurança (endereçar vulnerabilidades como XSS e CSRF) |
| 2. Design Detalhado & Modelagem | Definição da lógica de negócios e da modelagem de dados | SDD (Software Design Document) e definição de Trade-offs de Modelagem | Documentação e Pseudocódigo para criar uma ponte com o código final |

#### Etapa 3: Implementação (Codificação)

Fase onde o código é escrito, com base no Design.

| Sub-etapa | Descrição do Processo | Ferramentas e Conceitos | Práticas de Qualidade |
|-----------|----------------------|------------------------|----------------------|
| 1. Desenvolvimento | Escrita do código Front-end e Back-end | Uso de Callbacks, Promises e async/await | Priorizar a manutenção e a documentação contínua. Uso de TypeScript para código mais estruturado |
| 2. Segurança do Código | Proteger as funções de backend e evitar a exposição de segredos | Uso de Secret Manager para credenciais de terceiros | Manter segredos fora do código-fonte |

#### Etapa 4: Testes e Verificação

Fase para garantir que o software funciona e atende aos requisitos.

| Sub-etapa | Descrição do Processo | Tipos de Teste | Ferramentas |
|-----------|----------------------|----------------|-------------|
| 1. Testes Funcionais | Verificação da funcionalidade | Teste Unitário, Teste de Integração, Teste de Sistema | Test Cases são escritos para verificar a funcionalidade |
| 2. Testes de Qualidade | Confirma que mudanças recentes não afetam a funcionalidade existente | Teste de Regressão, Teste de Aceitação do Usuário (UAT) | Firebase Emulator Suite (para simular serviços localmente) |

#### Etapa 5: Implantação (Deployment)

Fase de lançamento do software para uso, usando práticas de automação.

| Sub-etapa | Descrição do Processo | Ambientes e Ferramentas | Pós-Deploy Imediato |
|-----------|----------------------|------------------------|---------------------|
| 1. Releases Iniciais | Lançamento da primeira versão funcional para um grupo seleto (Alpha release) | Firebase Hosting e Firebase CLI (firebase deploy) | Monitoramento dos logs |
| 2. Implantação de Produção | Versão estável disponibilizada para todos os usuários (General Availability) | Continuous Delivery (CD) automatiza o movimento do software através do SDLC | Segurança Pós-Deploy: Deploy das Regras de Segurança |

#### Etapa 6: Manutenção e Operação

O processo contínuo de suporte, otimização e extensão do software.

| Aspecto | Descrição da Manutenção Pós-Software | Práticas e Ferramentas |
|---------|-------------------------------------|------------------------|
| Monitoramento e Alertas | Acompanhamento do desempenho, uso e custos da aplicação | Uso de Dashboard e Alertas de Orçamento |
| Otimização de Custos/Performance | Otimizar operações caras, como chamadas de IA | Cache Agressivo dos Resultados e Engenharia de Prompt Eficiente |
| Correção e Evolução | Suporte, correção de bugs, e aplicação de novos features em ciclos iterativos | Uso de Tratamento de Erros para notificação proativa de falhas |

### 2. Etapas Independentes e em Paralelo (Gerenciamento de Código e Automação)

Estas atividades são contínuas e rodam em paralelo com as fases sequenciais, sendo essenciais para a flexibilidade do pipeline.

| Etapa Independente | Descrição | Comandos/Ferramentas | Benefício no Pipeline |
|-------------------|-----------|---------------------|----------------------|
| Controle de Versão (Version Control) | Rastreamento e gestão de mudanças no código-fonte, usando Git, um DVCS | git commit, git push, git clone | Permite recuperar versões mais antigas se houver erros |
| Gerenciamento de Branches | Desenvolver features ou correções de forma isolada | Branches, Merge | O trabalho pode ser revisado e aprovado via Pull Request |
| Integração Contínua (CI) | Prática onde o novo código é integrado à base de código frequentemente | Build automation servers que executam automaticamente testes | Garante que todos os componentes do código funcionem juntos |
| Entrega Contínua (CD) | O movimento automatizado do software através do SDLC | Pipelines que automatizam testes e deploy | Torna o processo de implantação mais rápido e menos propenso a erros |

## Como Usar Este Repositório

### 1. Clone o Repositório

```bash
git clone <URL-DO-SEU-REPOSITORIO>
cd ESTRUTURA-ENGENHARIA-CONTEXTO
```

### 2. Execute o Guia Interativo

```bash
python3 sdlc_guide.py
```

O guia irá:
- Fazer perguntas sequenciais sobre seu projeto
- Gerar documentos automaticamente nas pastas apropriadas
- Criar uma estrutura completa seguindo as melhores práticas do SDLC

### 3. Documentos Gerados

Os documentos são criados automaticamente em:

- **/docs**: Documentação formal
  - `URS.md`: User Requirement Specification
  - `architecture.md`: Documento de Arquitetura
  - `test_plan.md`: Plano de Testes

- **/guides**: Guias práticos
  - `implementation.md`: Guia de Implementação
  - `deployment.md`: Guia de Deployment
  - `maintenance.md`: Guia de Manutenção

### 4. Integração com Copilot

Este repositório segue as regras de engenharia de contexto definidas em `ESTRUTURA.TXT`:

- **Tarefas criativas** (design, arquitetura): top-k: 50-100, temp: 0.7-0.9
- **Tarefas literais** (código, APIs): top-k: 1-10, temp: 0.1-0.3
- **Documentação**: top-k: 20-40, temp: 0.4-0.6
- **Testes**: top-k: 10-30, temp: 0.2-0.4

## Estrutura de Pastas

```
/project-root
   ├── sdlc_guide.py        # Script interativo do SDLC
   ├── ESTRUTURA.TXT        # Regras de engenharia de contexto
   ├── requirements.txt     # Dependências do projeto
   ├── /docs                # Documentação formal
   ├── /videos              # Transcrições de vídeos
   ├── /urls                # Conteúdo de URLs
   ├── /code                # Código-fonte
   └── /guides              # Guias explicativos
```

## Fluxo de Trabalho Recomendado

1. **Inicialização**: Execute `sdlc_guide.py` e responda às perguntas
2. **Revisão**: Revise os documentos gerados em `/docs` e `/guides`
3. **Configuração**: Configure Git, CI/CD conforme os guias
4. **Desenvolvimento**: Siga as fases do SDLC sequencialmente
5. **Iteração**: Use as etapas paralelas (CI/CD) continuamente
6. **Manutenção**: Implemente monitoramento e alertas

## Referências

- [GitHub Copilot Best Practices](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
- [GitHub Copilot Coding Agent Concepts](https://docs.github.com/en/copilot/concepts/agents/coding-agent)

---

*Sistema SDLC Interativo - Estrutura Flexível para Criação de Software*
