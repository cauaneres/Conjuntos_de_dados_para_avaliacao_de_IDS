# Construção de conjuntos de dados para avaliação de sistemas de detecção de intrusão

Essa iniciação Científica se trata de uma construção de conjuntos de dados para ser feito a avalição em IDS. A criação desses datasets foram feitas em duas etapas, a primeira se trata de um ambiente de simulação de ataques com VMs (máquinas virtuais) dentro de uma mesma rede, uma VM atuando como atacante e outra como vítima. A segunda etapa foi a geração de dados sintéticos com IAs (inteligência artificial) generativas, com tecnicas de engenharia de prompt e com o auxílio dos conjuntos gerados na primera etapa. 

## Construção dos conjuntos no ambiente de simulação de ataques

Este ambiente de simulação de ataques foi contruindo dentro de uma máquina local, onde houve também a captura de seus dados, sendo um trafégo benigno. Foi executado pela VM atacante, ataques indíviduais de diferentes tipos e em conjuntos, levando a criação de datasets mais diversos. Com isso a VM vítima captura todo trafégo durante o ataque, que no final, gera um .CVS com as informações naquele intervalo que ocorreu os ataques. A duração dos ataques ficaram entre 5 a 15 minutos, levando em consideração que alguns desses ataques podem ocorrer em um tempo menor do que o proposto. Importante os créditos para o colega gustavodgbernardo, que ajudou bastante com a estruturação dessa etapa.

<img width="830" height="499" alt="image" src="https://github.com/user-attachments/assets/f7e18e43-78ee-44cd-9788-dfbfa3e7d060" />

## Geração de Dados Sintéticos com Inteligência Artificial

Feito a construção dos dados, os mesmos foram usados para a geração de dados sintéticos em IAs, foi usado o dataset do ataque DoS-Slowhttp e técnicas de enegenharia de prompt (Zero-Shot Prompting e One-Shot Prompting). Os dados criados no ambiente foram enviados em conjunto com os prompts de cada técnica separadamente e em duas intelegências Artificiais diferentes.

<img width="715" height="337" alt="image" src="https://github.com/user-attachments/assets/f25e051b-a0d7-4bbe-b099-e687d80b7e39" />

### Tecnologias Utilizadas

Ambiente:
* [Oracle Virtual Box 7.0](https://www.virtualbox.org).
* [Vagrant >=2.4.1](https://www.vagrantup.com).
* [Docker >= 27.3.1](https://docs.docker.com/engine/install/).
* [NFstream](https://www.nfstream.org).
* get-flow.py (captura o tráfego de rede da interface eth0, analisa os fluxos e salva todos os dados em um arquivo csv).


Ataques:
* [DoS-GoldenEye](https://github.com/jseidl/GoldenEye).
* [DoS-Hulk](https://github.com/R3DHULK/HULK).
* [DoS-slowloris](https://github.com/gkbrk/slowloris).
* [FTP-Patator](https://www.kali.org/tools/patator/https://github.com/lanjelot/patator).
* [SSH-Patator](https://www.kali.org/tools/patator/https://github.com/lanjelot/patator).
* DoS-Slowhttptest.
* nmap.

IAs Generativas:
* [ChatGpt](https://chatgpt.com/)
* [Gemini](https://gemini.google.com)

## Dependências e Versões Necessárias

* [Oracle Virtual Box 7.0](https://www.virtualbox.org).
* [Vagrant >=2.4.1](https://www.vagrantup.com).
* [Docker >= 27.3.1](https://docs.docker.com/engine/install/).
* [NFstream](https://www.nfstream.org).
* get-flow.py

## Como rodar o projeto ✅

Descreva o passo a passo necessário para rodar sua aplicação. Lembre-se: a pessoa nunca rodou seu projeto. Não tenha medo de detalhar o máximo possível. Isso é necessário!

Uma boa forma de descrever o passo a passo é:

```
Comando 1
```

Depois, rode o seguinte comando:

```
Comando 2
```

Deixe claro como a pessoa pode confirmar que a aplicação está rodando da forma correta. Pode ser com prints ou a mensagem que ela deve esperar.

## Observações

As pastas de ataques estão separados em duas, ataques inviduais e ataques combinados.

## Como rodar os testes

Explique como rodar os testes da aplicação. Exemplo de um comando usando Makefile para rodar os testes:

```
make test
```

## 📌 (Título) - Informações importantes sobre a aplicação (exemplo) 📌

Esse é o local para você preencher com outras informações que possam ser importantes para a aplicação. Coloquei um exemplo de título, mas você deve preencher de acordo com a necessidade do projeto. Pode ser que não seja necessário.

Um bom exemplo: se você estiver construindo uma API, liste as rotas da aplicação e quais serão os seus retornos. Isso facilita para quem vai consumir a API.


## ⚠️ Problemas enfrentados

Liste os problemas que você enfrentou construindo a aplicação e como você resolveu cada um deles. Você que desenvolveu o projeto é a pessoa que mais conhece/entende os possíveis problemas que uma pessoa pode enfrentar rodando a aplicação. Compartilhe esse conhecimento e facilite a vida da pessoa descrevendo-os.

Exemplo:

### Problema 1:
Descrição do problema
* Como solucionar: explicar a solução.
