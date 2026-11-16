# Padrão de engenharia do portfólio

## Objetivo

Manter o repositório de perfil claro, verificável, acessível, seguro e simples de atualizar. Este padrão orienta a documentação do portfólio; não impõe arquitetura única aos projetos independentes.

## Princípios

1. **Apresentação baseada em evidências:** distinguir funcionalidades implementadas, estudos em andamento e objetivos futuros.
2. **Coerência bilíngue:** manter fatos e limitações equivalentes nos READMEs em português e inglês.
3. **Escopo proporcional:** utilizar ferramentas e automação adequadas a um repositório documental.
4. **Integridade de referências:** verificar imagens, links e arquivos locais.
5. **Segurança:** não versionar credenciais, tokens, dados pessoais ou informações privadas.
6. **Manutenibilidade:** registrar alterações relevantes e remover redundância documental.
7. **Identidade preservada:** utilizar os ativos oficiais da marca sem alterações arbitrárias.

## Validação local

Requisitos: Python 3.12 ou superior, sem dependências externas.

```bash
python scripts/validate_profile.py
```

O validador verifica:
- existência dos READMEs em português e inglês;
- presença das referências obrigatórias ao banner e monograma;
- existência de links e imagens locais;
- referências locais confinadas ao diretório do repositório;
- sintaxe XML dos SVGs, elemento raiz, `viewBox` e título acessível.

A validação estrutural não avalia renderização visual, validade de links externos, correção linguística, precisão editorial ou testes dos projetos referenciados.

## CI

O workflow `Profile quality` executa o validador em pushes para `main`, Pull Requests direcionadas à `main` e execução manual. O workflow utiliza permissões somente de leitura para o conteúdo.

## Evolução

Mudanças relevantes no escopo, organização ou identidade devem ser registradas em `docs/decisions/`. Não declarar verificações aprovadas sem execução observável.
