# Meu padrão de engenharia para o portfólio

## Objetivo

Uso este documento para organizar os critérios técnicos que aplico aos repositórios que mantenho neste perfil. Meu objetivo é tornar cada projeto compreensível, verificável, seguro e reproduzível, sem padronizar artificialmente aplicações de tecnologias e escopos diferentes.

## Critérios que procuro manter

1. **Apresentação fiel:** descrevo o que realmente está implementado e separo protótipos, simulações e funcionalidades planejadas.
2. **Execução reproduzível:** documento runtimes, dependências, comandos e configuração local.
3. **Qualidade automatizada:** utilizo build, testes, lint ou validações de assets conforme o tipo de repositório.
4. **Segurança:** não versiono segredos nem dados pessoais e mantenho orientações de reporte privado.
5. **Arquitetura documentada:** registro componentes, limites, integrações e decisões relevantes.
6. **Manutenção:** acompanho dependências, alterações importantes e limitações conhecidas.
7. **Acessibilidade e internacionalização:** considero esses requisitos quando fazem parte do objetivo do projeto.

## Validação deste repositório

Executo a validação de assets e referências locais com:

```bash
python scripts/validate_profile.py
```

O workflow `Profile quality` executa esse comando em alterações na branch `main` e em Pull Requests direcionados a ela.

## Escopo e limites

Este repositório é meu perfil/portfólio. Não o trato como aplicação de produção e não aplico nele pipelines de build de backend que não existem neste projeto. Para cada projeto, registro os comandos específicos no README e no workflow correspondente.

## Evolução do padrão

Quando altero este padrão, documento o motivo em `docs/decisions/` e ajusto os workflows ou guias afetados. Não marco uma verificação como aprovada sem uma execução observável.
