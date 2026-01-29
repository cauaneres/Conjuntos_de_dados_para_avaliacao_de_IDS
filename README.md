# Construção de conjuntos de dados para avaliação de sistemas de detecção de intrusão

Esta Iniciação Científica trata da construção de conjuntos de dados para a realização da avaliação em IDS. A criação desses datasets foi feita em duas etapas. A primeira consiste em um ambiente de simulação de ataques com VMs (máquinas virtuais) dentro de uma mesma rede, com uma VM atuando como atacante e outra como vítima. A segunda etapa foi a geração de dados sintéticos com IAs (inteligência artificial) generativas, utilizando técnicas de engenharia de prompt e com o auxílio dos conjuntos gerados na primeira etapa. Este repositório contém os scripts, instruções e comandos necessários para reproduzir os experimentos descritos no relatório de Iniciação Científica.

## Construção dos conjuntos no ambiente de simulação de ataques

Este ambiente de simulação de ataques foi construído dentro de uma máquina local, onde também houve a captura de seus dados, sendo um tráfego benigno. Foram executados, pela VM atacante, ataques individuais de diferentes tipos e em conjunto, levando à criação de datasets mais diversos. Com isso, a VM vítima captura todo o tráfego durante o ataque, o que, ao final, gera um arquivo .CSV com as informações do intervalo em que ocorreram os ataques. A duração dos ataques ficou entre 5 e 15 minutos, levando em consideração que alguns desses ataques podem ocorrer em um tempo menor do que o proposto. Importantes os créditos ao colega gustavodgbernardo, que ajudou bastante na estruturação dessa etapa.

<img width="830" height="499" alt="image" src="https://github.com/user-attachments/assets/f7e18e43-78ee-44cd-9788-dfbfa3e7d060" />

## Geração de dados sintéticos com inteligência artificial

Após a construção dos dados, os mesmos foram utilizados para a geração de dados sintéticos em IAs. Foi usado o dataset do ataque DoS-Slowhttp e técnicas de engenharia de prompt (Zero-Shot Prompting e One-Shot Prompting). Os dados criados no ambiente foram enviados em conjunto com os prompts de cada técnica, separadamente, e em duas inteligências artificiais diferentes.

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
* [ChatGpt](https://chatgpt.com/)

## Como criar o ambiente de simulação de ataques 

### Criação das VMs

Para criar as máquinas virtuais, utiliza-se o Vagrant. Ao executar o comando abaixo, as duas VMs serão criadas; o Kali abrirá uma janela solicitando usuário e senha, ambos sendo "vagrant".

```
$ vagrant up
```

No caso da VM Ubuntu, nenhuma janela será aberta e, para acessá-la, basta utilizar o comando:

```
$ vagrant ssh ubuntu16
```
### Coleta dos dados locais

Na coleta dos dados da máquina local (tráfego benigno), é realizada a captura de fluxos normais. **Essa etapa exige mais atenção, pois serão captadas informações da sua rede, como endereços IP e páginas visitadas**. Após a coleta dos dados, será necessário realizar a anonimização das informações.

O primeiro passo será trocar, no arquivo get-flow.py, a palavra "rede" pela interface de rede local da sua máquina, executando o seguinte comando para obter as informações necessárias para a substituição:

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

Agora, deve-se pegar a interface de rede local (que normalmente está associada a endereços 192.168.xx), que no exemplo é enp9s0. Logo, o arquivo get-flow.py ficará da seguinte maneira:

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
Após alguns minutos, espera-se que apareça na pasta do projeto um arquivo chamado same_attacks.csv. Esse arquivo contém os fluxos de dados gerados a partir dos pacotes de rede, utilizando o NFstream.

### Coleta dos dados da VM vítima

Para entrar na VM que será atacada, executa o comando:

```
$ vagrant ssh ubuntu16
```
Depois de entrar, edite o arquivo get-flow.py e troque "rede" pela interface da rede local.

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
É importante anotar o IP da VM vítima, pois será o IP atacado pelo Kali.

Agora será construída a imagem da vítima no Docker.
```
sudo docker build -t collect_attacks .
```

Em seguida, execute.
```
sudo docker run -d --network host --user root --rm -v "${PWD}":/home/python/ collect_attacks
```
Aguardando alguns minutos, o arquivo same_attacks deve ter sido criado; caso contrário, algo deu errado.

### Executando os ataques

Depois de concluir os passos anteriores, vamos dar início aos ataques.

Primeiramente, entre na VM KaliLinux com o usuário e a senha citados, abra um terminal e execute o comando:

```
$ ifconfig
```

**Anote o IP desta VM; esse passo é muito importante.**

O IP da VM vítima é muito importante nesta etapa, juntamente com a anotação do horário exato de início e fim de cada ataque. Alguns ataques param apenas com Ctrl+C. Recomenda-se um intervalo de 5 a 15 minutos para cada ataque (pode ser mais ou menos, dependendo da sua proposta).

Substitua "IP-atacado" pelo IP da VM vítima (ubuntu16). Seguem abaixo os ataques realizados:

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

Novamente, deixo os créditos ao colega **gustavodgbernardo** pela ajuda nessa estruturação.

## Como gerar dados sintéticos com IA 

Para começar, vamos utilizar o ChatGPT, pois foi onde se obtiveram os melhores resultados, em comparação com o Gemini. O Gemini não criava os conjuntos, apenas apresentava o passo a passo de como construir um dataset.

Primeiro, pode-se tentar a primeira estratégia de engenharia de prompt, **Zero-Shot Prompting**. Juntamente com o conjunto de dados, vamos utilizar o seguinte prompt:
```
"Gere um Dataset de um ataque Dos-Slowhttp em formato de CSV, usarei
esse arquivo para treinar um modelo de detecção de intrusão."
```
Dependendo dos resultados, ajustes na frase e a mudança da língua podem ajudar a buscar resultados melhores.

A segunda estratégia é o **One-Shot Prompting**, que se mostrou mais eficiente que a anterior. Podemos usar o seguinte prompt:
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
A dica da estratégia anterior vale para esta também. Com tentativas e polimento, os resultados podem ser melhores.

## Observações

Os ataques descritos neste repositório foram executados exclusivamente em ambiente controlado e para fins acadêmicos.

Os comandos apresentados são para o sistema operacional Linux. Caso seja utilizado outro sistema, os comandos podem mudar, como no caso do Docker, por exemplo.

No caso de executar ataques separados, é recomendável que, para cada ataque, seja criado um arquivo .CSV individual. Já nos casos de ataques combinados (A+B+C), também deve ser gerado um arquivo .CSV separado, um para cada combinação.

A cada novo arquivo .CSV gerado, ele sempre terá o nome **"same_attacks"**. Recomenda-se que, ao final de cada ataque, o nome seja alterado para evitar confusão.
