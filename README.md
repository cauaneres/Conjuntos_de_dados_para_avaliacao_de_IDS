# Construção de conjuntos de dados para avaliação de sistemas de detecção de intrusão

Essa iniciação Científica se trata de uma construção de conjuntos de dados para ser feito a avalição em IDS. A criação desses datasets foram feitas em duas etapas, a primeira se trata de um ambiente de simulação de ataques com VMs (máquinas virtuais) dentro de uma mesma rede, uma VM atuando como atacante e outra como vítima. A segunda etapa foi a geração de dados sintéticos com IAs (inteligência artificial) generativas, com tecnicas de engenharia de prompt e com o auxílio dos conjuntos gerados na primera etapa. 

## Construção dos conjuntos no ambiente de simulação de ataques

Este ambiente de simulação de ataques foi contruindo dentro de uma máquina local, onde houve também a captura de seus dados, sendo um trafégo benigno. Foi executado pela VM atacante, ataques indíviduais de diferentes tipos e em conjuntos, levando a criação de datasets mais diversos. Com isso a VM vítima captura todo trafégo durante o ataque, que no final, gera um .CVS com as informações naquele intervalo que ocorreu os ataques. A duração dos ataques ficaram entre 5 a 15 minutos, levando em consideração que alguns desses ataques podem ocorrer em um tempo menor do que o proposto. Importante os créditos para o colega gustavodgbernardo, que ajudou bastante com a estruturação dessa etapa.

<img width="830" height="499" alt="image" src="https://github.com/user-attachments/assets/f7e18e43-78ee-44cd-9788-dfbfa3e7d060" />

## Geração de Dados Sintéticos com Inteligência Artificial

Feito a construção dos dados, os mesmos foram usados para a geração de dados sintéticos em IAs, foi usado o dataset do ataque DoS-Slowhttp e técnicas de enegenharia de prompt (Zero-Shot Prompting e One-Shot Prompting). Os dados criados no ambiente foram enviados em conjunto com os prompts de cada técnica separadamente e em duas intelegências Artificiais diferentes.

<img width="715" height="337" alt="image" src="https://github.com/user-attachments/assets/f25e051b-a0d7-4bbe-b099-e687d80b7e39" />

## Tecnologias Utilizadas

#### Ambiente:
* [Oracle Virtual Box 7.0](https://www.virtualbox.org).
* [Vagrant >=2.4.1](https://www.vagrantup.com).
* [Docker >= 27.3.1](https://docs.docker.com/engine/install/).
* [NFstream](https://www.nfstream.org).
* get-flow.py (captura o tráfego de rede da interface eth0, analisa os fluxos e salva todos os dados em um arquivo csv).


#### Ataques:
* [DoS-GoldenEye](https://github.com/jseidl/GoldenEye).
* [DoS-Hulk](https://github.com/R3DHULK/HULK).
* [DoS-slowloris](https://github.com/gkbrk/slowloris).
* [FTP-Patator](https://www.kali.org/tools/patator/https://github.com/lanjelot/patator).
* [SSH-Patator](https://www.kali.org/tools/patator/https://github.com/lanjelot/patator).
* DoS-Slowhttptest.
* nmap.

#### IAs Generativas:
* [ChatGpt](https://chatgpt.com/)
* [Gemini](https://gemini.google.com)

## Dependências e Versões Necessárias

* [Oracle Virtual Box 7.0](https://www.virtualbox.org).
* [Vagrant >=2.4.1](https://www.vagrantup.com).
* [Docker >= 27.3.1](https://docs.docker.com/engine/install/).
* [NFstream](https://www.nfstream.org).
* get-flow.py

## Como criar o ambiente de simulação de ataques ✅

### Criação das VMs

Para criar as máquinas virtuais, se usa o Vagrant. Executando o comando abaixo, as duas VMs serão criadas,o Kali abrirá uma janela pedindo usuário e senha, ambas são "vagrant". 

```
$ vagrant up
```

No caso da VM ubuntu, não abrirá a janela e para acessar basta usar o comando:

```
$ vagrant ssh ubuntu16
```
### Coleta dos dados Locais

Na coleta dos dados da máquina local(tráfego benigno), é realizada uma captura de fluxos normais. **Essa etapa exige mais atenção, pois serão captadas em sua rede informações como endereços de ips e páginas visitadas**. Depois da coleta dos dados, será necessário fazer anonimização de dados.

Primeiro passo sera trocar no arquivo *get-flow.py* a palavra "rede" para interface de rede local de sua máquina, executando o seguinte comando:

```
$ ifconfig
```

Exemplo:

```
br-ff73f8fa2eae: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        RX packets 22534  bytes 1218433 (1.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 44537  bytes 71349934 (71.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp9s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.100  netmask 255.255.255.0  broadcast 192.168.0.255
        ether 3c:7c:3f:7c:4b:3b  txqueuelen 1000  (Ethernet)
        RX packets 18083597  bytes 15420472993 (15.4 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9591298  bytes 4193171594 (4.1 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 413446  bytes 40541720 (40.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 413446  bytes 40541720 (40.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Agora devesse pegar a rede local (que normalmente é 192.168.xx), que no exemplo é *enp9s0* logo o arquivo *get-flow.py* ficara da seguinte maneira:

```
from nfstream import NFStreamer

online_streamer = NFStreamer(source="enp9s0", statistical_analysis = True, idle_timeout=60, active_timeout=600)

total_flows_count = online_streamer.to_csv(path="same_attacks.csv", columns_to_anonymize=[], flows_per_file=0, rotate_files=0)
```
**É de extrema importância editar e trocar corretamente o nome antes de construir e executar uma imagem!**

Depois de editar o arquivo, construa a imagem docker:

```
sudo docker build -t collect_attacks .
```

Em seguida, execute:

```
sudo docker run -d --network host --user root --rm -v "${PWD}":/home/python/ collect_attacks
```
Ápos alguns minutos, esperasse que apareça na pasta do projeto um arquivo chamado *same_attacks.csv*, o seguinte arquivo contém os fluxos de dados gerados através dos pacotes de rede, utilizando o NFstream.

### Coleta dos dados da VM vítima

Para entrar na VM que será atacada, executa o comando:

```
$ vagrant ssh ubuntu16
```
Depois de dentro, edite o arquivo *get-glow.py* e troque "rede" pela interface da rede local

Exemplo:
```
vagrant@ubuntu-xenial:~$ ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:30:23:d6:2f
          inet addr:172.17.0.1  Bcast:172.17.255.255  Mask:255.255.0.0
          inet6 addr: fe80::42:30ff:fe23:d62f/64 Scope:Link
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:21289 errors:0 dropped:0 overruns:0 frame:0
          TX packets:44245 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:897111 (897.1 KB)  TX bytes:70794584 (70.7 MB)

enp0s3    Link encap:Ethernet  HWaddr 02:be:82:6b:cc:1d
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::be:82ff:fe6b:cc1d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:51157 errors:0 dropped:0 overruns:0 frame:0
          TX packets:24416 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:71310993 (71.3 MB)  TX bytes:1751755 (1.7 MB)

enp0s8    Link encap:Ethernet  HWaddr 08:00:27:c6:7d:f2
          inet addr:192.168.0.148  Bcast:192.168.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1247316 errors:0 dropped:0 overruns:0 frame:0
          TX packets:115384 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1287039569 (1.2 GB)  TX bytes:9998727 (9.9 MB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

vagrant@ubuntu-xenial:~$ vi get-flow.py

from nfstream import NFStreamer

online_streamer = NFStreamer(source="enp0s8", statistical_analysis = True, idle_timeout=60, active_timeout=600)

total_flows_count = online_streamer.to_csv(path="same_attacks.csv", columns_to_anonymize=[], flows_per_file=0, rotate_files=0)
```
Importante anotar o IP da VM vítima, pois será o IP atacado pelo Kali.

Agora será construido a imagem da vítima no docker.
```
sudo docker build -t collect_attacks .
```

Em seguida, execute.
```
sudo docker run -d --network host --user root --rm -v "${PWD}":/home/python/ collect_attacks
```
Aguardando alguns minutos, o arquivo *same_atacks* deve ter sido criado, caso contrário, houve algo de errado.

### Executando os ataques

Depois de concluir os passos anteriores, vamos dar início aos ataques

Primeiramente entre na VM linux com o usuario e senha citados e abra um terminal execute o comando:

```
$ ifconfig
```

**E anote o IP desta VM é muito importante esse passo**

O IP da VM vítima é muito importante nesta etapa, juntamente com anotação do horario exato de início e fim de cada ataque. Alguns ataques param apenas com *Crtl+c*, um intervalo de 5 a 15 minutos para cada ataque (pode ser mais ou menos, dependo da sua proposta).

Substitua "IP-atacado" pelo o IP da VM vítima (ubuntu16), segue abaixo os ataques realizados:

##### DoS-Slowhttptest

```
slowhttptest -c 1000 -H -g -o slowhttp -i 10 -r 200 -t GET -u http://<IP-atacado> -x 24 -p 3
```

#### DoS-GoldenEye

```
$ cd GoldenEye
$ ./goldeneye.py http://<IP-atacado> -w 1 -s 10 -m get
```

#### DoS-Hulk

```
$ cd HULK
$ python hulk.py
```
<IP-atacado>

#### DoS-slowloris

```
slowloris <IP-atacado>
```

#### FTP-Patator

```
patator ftp_login host=<IP-atacado> user=FILE0 0=top-usernames-shortlist.txt password=FILE1 1=darkweb2017-top10000.txt -x ignore:mesg='Login incorrect.' -x ignore,reset,retry:code=500
```

#### SSH-Patator

```
patator ssh_login host=<IP-atacado> user=FILE0 0=top-usernames-shortlist.txt password=FILE1 1=darkweb2017-top10000.txt -x ignore:mesg='Authentication failed.'
```

#### nmap

```
sudo nmap -sS <IP-atacado>
sudo nmap -sT <IP-atacado>
sudo nmap -sF <IP-atacado>
sudo nmap -sX <IP-atacado>
sudo nmap -sN <IP-atacado>
sudo nmap -sP <IP-atacado>
sudo nmap -sV <IP-atacado>
sudo nmap -sU <IP-atacado>
sudo nmap -sO <IP-atacado>
sudo nmap -sA <IP-atacado>
sudo nmap -sW <IP-atacado>
sudo nmap -sR <IP-atacado>
sudo nmap -sL <IP-atacado>
sudo nmap -B <IP-atacado>
```

## Como gerar dados sintéticos com IA ✅

Para começar, vamos para o *chatgpt*, pois foi gerado os melhores resultados, comparado com o Gemini. O Gemini não criava os conjuntos, apenas passava o passo a passo de como contruir um dataset

Primeiro pode tentar a primeira estratégia de engenharia de prompt, Zero-Short Prompting. Juntamente com o conjunto de dados vamos usar o seguinte prompt:
```
"Gere um Dataset de um ataque Dos-Slowhttp em formato de CSV, usarei
esse arquivo para treinar um modelo de detecção de intrusão."
```
Depedendo dos resultados, ajustes na frase e mudança da lingua podem ajudar buscar resultado melhores.

A segunda estratégia é o One-Short Prompting, que mostrou ser mais efeciente que a anterior. Podemos usar o seguinte prompt:
```
"Você é um profissional da área de Cibersegurança a 10 anos,
está fazendo um estudo de treinar modelos em detecção de intrusão.
Sendo assim precisa gerar um Dataset do ataque Dos-Slowhttp em
uma rede real para melhor precisão dos dados.
Você vai usar os seguintes critérios:
- Dataset deve ter no mínimo 150 linhas.
- Deve ser o mais próximo possível da realidade.
- Conter dados de tráfego normal.
- Conter dados de ataque.
- A distribuição de dados de ataque e tráfego normal deve ser aleatória,
conforme sua rede nesse cenário.
- Você está usando sua rede de casa e está sozinho.
- Está usando duas VMs, uma Ubuntu para receber os ataques e uma
Kali para atacar.
Exemplo de um Dataset Dos-Slowhttp: "
```
A dica da estratégia anterior, vale pra essa mesma. Com tentativas e polimento, o resultados podem ser melhores.

## Observações

As pastas de ataques estão separados em duas, ataques inviduais e ataques combinados.

### Como rodar os testes

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
