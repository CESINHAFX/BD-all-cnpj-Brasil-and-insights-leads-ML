#!/usr/bin/env python3
"""
SDLC Interactive Guide
======================
Guia interativo para conduzir usuários através do ciclo de vida de desenvolvimento
de software (SDLC) com questões sequenciais baseadas na estrutura do repositório.
"""

import json
import datetime
from pathlib import Path


class SDLCGuide:
    """Guia interativo do ciclo SDLC com engenharia de contexto."""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.responses = {}
        self.current_phase = None
        
    def welcome(self):
        """Mensagem de boas-vindas."""
        print("=" * 80)
        print("BEM-VINDO AO GUIA INTERATIVO SDLC")
        print("Estrutura de Engenharia de Contexto para Desenvolvimento de Software")
        print("=" * 80)
        print("\nEste guia irá conduzi-lo através das fases do SDLC:")
        print("1. Requisitos e Análise")
        print("2. Design e Arquitetura")
        print("3. Implementação (Codificação)")
        print("4. Testes e Verificação")
        print("5. Implantação (Deployment)")
        print("6. Manutenção e Operação")
        print("\nVamos começar!\n")
        
    def phase1_requirements(self):
        """Fase 1: Requisitos e Análise."""
        self.current_phase = "requirements"
        print("\n" + "=" * 80)
        print("FASE 1: REQUISITOS E ANÁLISE")
        print("=" * 80)
        print("\nNesta fase, vamos definir o escopo e as necessidades do projeto.\n")
        
        questions = [
            {
                "key": "project_name",
                "question": "Qual é o nome do seu projeto?",
                "folder": "/"
            },
            {
                "key": "project_purpose",
                "question": "Qual é o propósito principal do software?",
                "folder": "/docs"
            },
            {
                "key": "target_users",
                "question": "Quem são os usuários finais/stakeholders?",
                "folder": "/docs"
            },
            {
                "key": "main_features",
                "question": "Liste as funcionalidades principais (separe por vírgula):",
                "folder": "/docs"
            },
            {
                "key": "success_criteria",
                "question": "Quais são os critérios de sucesso do projeto?",
                "folder": "/docs"
            },
            {
                "key": "business_rules",
                "question": "Descreva as regras de negócio principais:",
                "folder": "/docs"
            }
        ]
        
        responses = self._ask_questions(questions)
        self.responses["phase1"] = responses
        
        # Criar documento URS
        self._create_urs_document(responses)
        print("\n✓ Documento URS (User Requirement Specification) criado em /docs/URS.md")
        
    def phase2_design(self):
        """Fase 2: Design e Arquitetura."""
        self.current_phase = "design"
        print("\n" + "=" * 80)
        print("FASE 2: DESIGN E ARQUITETURA")
        print("=" * 80)
        print("\nVamos projetar a arquitetura do sistema.\n")
        
        questions = [
            {
                "key": "architecture_type",
                "question": "Tipo de arquitetura (ex: SOA, Microservices, Monolith):",
                "folder": "/docs"
            },
            {
                "key": "tech_stack",
                "question": "Tecnologias principais (linguagens, frameworks):",
                "folder": "/code"
            },
            {
                "key": "database_type",
                "question": "Tipo de banco de dados (ex: SQL, NoSQL, Firestore):",
                "folder": "/code"
            },
            {
                "key": "data_model",
                "question": "Descreva a modelagem de dados principal:",
                "folder": "/code"
            },
            {
                "key": "security_requirements",
                "question": "Requisitos de segurança (ex: autenticação, criptografia):",
                "folder": "/docs"
            },
            {
                "key": "scalability_needs",
                "question": "Necessidades de escalabilidade:",
                "folder": "/docs"
            }
        ]
        
        responses = self._ask_questions(questions)
        self.responses["phase2"] = responses
        
        # Criar documento de arquitetura
        self._create_architecture_document(responses)
        print("\n✓ Documento de Arquitetura criado em /docs/architecture.md")
        
    def phase3_implementation(self):
        """Fase 3: Implementação."""
        self.current_phase = "implementation"
        print("\n" + "=" * 80)
        print("FASE 3: IMPLEMENTAÇÃO (CODIFICAÇÃO)")
        print("=" * 80)
        print("\nVamos definir os detalhes da implementação.\n")
        
        questions = [
            {
                "key": "coding_standards",
                "question": "Padrões de código a seguir (ex: PEP 8, ESLint):",
                "folder": "/code"
            },
            {
                "key": "dependencies",
                "question": "Dependências principais do projeto:",
                "folder": "/"
            },
            {
                "key": "version_control",
                "question": "Estratégia de controle de versão (ex: Git Flow, Trunk-based):",
                "folder": "/"
            },
            {
                "key": "secret_management",
                "question": "Como serão gerenciados os segredos (ex: .env, Secret Manager):",
                "folder": "/code"
            },
            {
                "key": "documentation_approach",
                "question": "Abordagem de documentação (ex: docstrings, JSDoc):",
                "folder": "/code"
            }
        ]
        
        responses = self._ask_questions(questions)
        self.responses["phase3"] = responses
        
        # Criar guia de implementação
        self._create_implementation_guide(responses)
        print("\n✓ Guia de Implementação criado em /guides/implementation.md")
        
    def phase4_testing(self):
        """Fase 4: Testes e Verificação."""
        self.current_phase = "testing"
        print("\n" + "=" * 80)
        print("FASE 4: TESTES E VERIFICAÇÃO")
        print("=" * 80)
        print("\nVamos definir a estratégia de testes.\n")
        
        questions = [
            {
                "key": "test_types",
                "question": "Tipos de testes a implementar (Unit, Integration, E2E):",
                "folder": "/code"
            },
            {
                "key": "test_framework",
                "question": "Framework de testes (ex: pytest, Jest):",
                "folder": "/code"
            },
            {
                "key": "coverage_target",
                "question": "Meta de cobertura de código (%):",
                "folder": "/code"
            },
            {
                "key": "ci_tool",
                "question": "Ferramenta de CI (ex: GitHub Actions, Jenkins):",
                "folder": "/"
            },
            {
                "key": "test_environment",
                "question": "Ambiente de testes (ex: Firebase Emulator, Docker):",
                "folder": "/code"
            }
        ]
        
        responses = self._ask_questions(questions)
        self.responses["phase4"] = responses
        
        # Criar plano de testes
        self._create_test_plan(responses)
        print("\n✓ Plano de Testes criado em /docs/test_plan.md")
        
    def phase5_deployment(self):
        """Fase 5: Implantação."""
        self.current_phase = "deployment"
        print("\n" + "=" * 80)
        print("FASE 5: IMPLANTAÇÃO (DEPLOYMENT)")
        print("=" * 80)
        print("\nVamos planejar a implantação do sistema.\n")
        
        questions = [
            {
                "key": "hosting_platform",
                "question": "Plataforma de hospedagem (ex: Firebase, AWS, Heroku):",
                "folder": "/docs"
            },
            {
                "key": "deployment_strategy",
                "question": "Estratégia de deploy (ex: Blue-Green, Rolling):",
                "folder": "/docs"
            },
            {
                "key": "cd_pipeline",
                "question": "Pipeline de CD (ex: GitHub Actions, GitLab CI):",
                "folder": "/"
            },
            {
                "key": "monitoring_tools",
                "question": "Ferramentas de monitoramento (ex: CloudWatch, Datadog):",
                "folder": "/docs"
            },
            {
                "key": "rollback_strategy",
                "question": "Estratégia de rollback em caso de falhas:",
                "folder": "/docs"
            }
        ]
        
        responses = self._ask_questions(questions)
        self.responses["phase5"] = responses
        
        # Criar guia de deployment
        self._create_deployment_guide(responses)
        print("\n✓ Guia de Deployment criado em /guides/deployment.md")
        
    def phase6_maintenance(self):
        """Fase 6: Manutenção e Operação."""
        self.current_phase = "maintenance"
        print("\n" + "=" * 80)
        print("FASE 6: MANUTENÇÃO E OPERAÇÃO")
        print("=" * 80)
        print("\nVamos definir a estratégia de manutenção.\n")
        
        questions = [
            {
                "key": "monitoring_metrics",
                "question": "Métricas principais a monitorar:",
                "folder": "/docs"
            },
            {
                "key": "alert_strategy",
                "question": "Estratégia de alertas e notificações:",
                "folder": "/docs"
            },
            {
                "key": "backup_strategy",
                "question": "Estratégia de backup de dados:",
                "folder": "/docs"
            },
            {
                "key": "cost_optimization",
                "question": "Estratégias de otimização de custos:",
                "folder": "/docs"
            },
            {
                "key": "support_process",
                "question": "Processo de suporte e correção de bugs:",
                "folder": "/guides"
            }
        ]
        
        responses = self._ask_questions(questions)
        self.responses["phase6"] = responses
        
        # Criar guia de manutenção
        self._create_maintenance_guide(responses)
        print("\n✓ Guia de Manutenção criado em /guides/maintenance.md")
        
    def _ask_questions(self, questions):
        """Faz perguntas ao usuário e coleta respostas."""
        responses = {}
        for q in questions:
            print(f"\n[Pasta: {q['folder']}]")
            answer = input(f"{q['question']}\n> ").strip()
            responses[q['key']] = answer
        return responses
        
    def _create_urs_document(self, responses):
        """Cria documento URS."""
        docs_dir = self.project_root / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        content = f"""# User Requirement Specification (URS)

**Projeto:** {responses.get('project_name', 'N/A')}
**Data:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Propósito do Software

{responses.get('project_purpose', 'N/A')}

## 2. Usuários e Stakeholders

{responses.get('target_users', 'N/A')}

## 3. Funcionalidades Principais

{responses.get('main_features', 'N/A')}

## 4. Critérios de Sucesso

{responses.get('success_criteria', 'N/A')}

## 5. Regras de Negócio

{responses.get('business_rules', 'N/A')}

---
*Documento gerado automaticamente pelo SDLC Guide*
"""
        
        with open(docs_dir / "URS.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    def _create_architecture_document(self, responses):
        """Cria documento de arquitetura."""
        docs_dir = self.project_root / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        content = f"""# Software Architecture Document

**Projeto:** {self.responses['phase1'].get('project_name', 'N/A')}
**Data:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Tipo de Arquitetura

{responses.get('architecture_type', 'N/A')}

## 2. Stack Tecnológico

{responses.get('tech_stack', 'N/A')}

## 3. Banco de Dados

**Tipo:** {responses.get('database_type', 'N/A')}

**Modelagem de Dados:**
{responses.get('data_model', 'N/A')}

## 4. Requisitos de Segurança

{responses.get('security_requirements', 'N/A')}

## 5. Escalabilidade

{responses.get('scalability_needs', 'N/A')}

---
*Documento gerado automaticamente pelo SDLC Guide*
"""
        
        with open(docs_dir / "architecture.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    def _create_implementation_guide(self, responses):
        """Cria guia de implementação."""
        guides_dir = self.project_root / "guides"
        guides_dir.mkdir(exist_ok=True)
        
        content = f"""# Guia de Implementação

**Projeto:** {self.responses['phase1'].get('project_name', 'N/A')}
**Data:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Padrões de Código

{responses.get('coding_standards', 'N/A')}

## 2. Dependências

{responses.get('dependencies', 'N/A')}

## 3. Controle de Versão

{responses.get('version_control', 'N/A')}

## 4. Gerenciamento de Segredos

{responses.get('secret_management', 'N/A')}

## 5. Documentação

{responses.get('documentation_approach', 'N/A')}

---
*Documento gerado automaticamente pelo SDLC Guide*
"""
        
        with open(guides_dir / "implementation.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    def _create_test_plan(self, responses):
        """Cria plano de testes."""
        docs_dir = self.project_root / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        content = f"""# Plano de Testes

**Projeto:** {self.responses['phase1'].get('project_name', 'N/A')}
**Data:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Tipos de Testes

{responses.get('test_types', 'N/A')}

## 2. Framework de Testes

{responses.get('test_framework', 'N/A')}

## 3. Meta de Cobertura

{responses.get('coverage_target', 'N/A')}%

## 4. Integração Contínua

{responses.get('ci_tool', 'N/A')}

## 5. Ambiente de Testes

{responses.get('test_environment', 'N/A')}

---
*Documento gerado automaticamente pelo SDLC Guide*
"""
        
        with open(docs_dir / "test_plan.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    def _create_deployment_guide(self, responses):
        """Cria guia de deployment."""
        guides_dir = self.project_root / "guides"
        guides_dir.mkdir(exist_ok=True)
        
        content = f"""# Guia de Deployment

**Projeto:** {self.responses['phase1'].get('project_name', 'N/A')}
**Data:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Plataforma de Hospedagem

{responses.get('hosting_platform', 'N/A')}

## 2. Estratégia de Deployment

{responses.get('deployment_strategy', 'N/A')}

## 3. Pipeline de CD

{responses.get('cd_pipeline', 'N/A')}

## 4. Monitoramento

{responses.get('monitoring_tools', 'N/A')}

## 5. Estratégia de Rollback

{responses.get('rollback_strategy', 'N/A')}

---
*Documento gerado automaticamente pelo SDLC Guide*
"""
        
        with open(guides_dir / "deployment.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    def _create_maintenance_guide(self, responses):
        """Cria guia de manutenção."""
        guides_dir = self.project_root / "guides"
        guides_dir.mkdir(exist_ok=True)
        
        content = f"""# Guia de Manutenção e Operação

**Projeto:** {self.responses['phase1'].get('project_name', 'N/A')}
**Data:** {datetime.datetime.now().strftime('%Y-%m-%d')}

## 1. Métricas de Monitoramento

{responses.get('monitoring_metrics', 'N/A')}

## 2. Alertas e Notificações

{responses.get('alert_strategy', 'N/A')}

## 3. Backup de Dados

{responses.get('backup_strategy', 'N/A')}

## 4. Otimização de Custos

{responses.get('cost_optimization', 'N/A')}

## 5. Processo de Suporte

{responses.get('support_process', 'N/A')}

---
*Documento gerado automaticamente pelo SDLC Guide*
"""
        
        with open(guides_dir / "maintenance.md", "w", encoding="utf-8") as f:
            f.write(content)
            
    def save_session(self):
        """Salva a sessão do SDLC em JSON."""
        session_file = self.project_root / "sdlc_session.json"
        with open(session_file, "w", encoding="utf-8") as f:
            json.dump(self.responses, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Sessão salva em {session_file}")
        
    def run(self):
        """Executa o guia interativo completo."""
        self.welcome()
        
        # Executar todas as fases
        self.phase1_requirements()
        self.phase2_design()
        self.phase3_implementation()
        self.phase4_testing()
        self.phase5_deployment()
        self.phase6_maintenance()
        
        # Salvar sessão
        self.save_session()
        
        print("\n" + "=" * 80)
        print("SDLC GUIDE COMPLETO!")
        print("=" * 80)
        print("\nTodos os documentos foram gerados nas pastas apropriadas:")
        print("  - /docs: Documentação de requisitos, arquitetura e testes")
        print("  - /guides: Guias de implementação, deployment e manutenção")
        print("\nPróximos passos:")
        print("  1. Revisar e refinar os documentos gerados")
        print("  2. Configurar o controle de versão (Git)")
        print("  3. Configurar CI/CD pipeline")
        print("  4. Começar a implementação seguindo os guias")
        print("\nBoa sorte com seu projeto!")
        print("=" * 80)


if __name__ == "__main__":
    guide = SDLCGuide()
    guide.run()
