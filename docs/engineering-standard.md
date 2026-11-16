# Padrão de engenharia do portfólio

## Objetivo

Manter o repositório de perfil claro, verificável, acessível, seguro e simples de atualizar. O padrão orienta a documentação deste repositório; não impõe uma arquitetura única aos seis projetos independentes.

## Princípios

1. **Apresentação baseada em evidências:** distinguir funcionalidades implementadas, estudos em andamento e objetivos futuros.
2. **Coerência bilíngue:** manter fatos e limitações equivalentes nos READMEs em português e inglês.
3. **Escopo proporcional:** utilizar ferramentas e automação adequadas a um repositório documental.
4. **Integridade de referências:** verificar imagens, links e arquivos locais.
5. **Segurança:** não versionar credenciais, tokens, dados pessoais ou informações privadas.
6. **Manutenibilidade:** registrar alterações relevantes e remover redundância documental.
7. **Identidade preservada:** usar os ativos oficiais de marca sem alterações arbitrárias.

## Validação local

Requisitos: Python 3.12 ou superior, sem dependências externas.

```bash
python scripts/validate_profile.py
```

O validador verifica:
- existência dos READMEs em português e inglês;
- presença das referências obrigatórias ao banner e monograma;
- existência de links e imagens locais;
- impedimento de referências locais que escapem do diretório do repositório;
- sintaxe XML dos SVGs, elemento raiz, `viewBox` e título acessível.

A validação estrutural não avalia a qualidade visual renderizada, validade de links externos, correção linguística, precisão de conteúdo ou testes dos projetos referenciados.

## CI

O workflow `Profile quality` executa o validador em pushes para `main`, Pull Requests direcionadas à `main` e execução manual. O workflow utiliza permissões somente de leitura para o conteúdo.

## Evolução

Mudanças relevantes no escopo, na organização ou na identidade devem ser registradas em `docs/decisions/`. Não declarar checks aprovados sem observar a execução correspondente.
