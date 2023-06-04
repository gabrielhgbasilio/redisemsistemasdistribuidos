# redisemsistemasdistribuidos
Prática de Frameworks e Bibliotecas para Sistemas Distribuídos Utilizando Redis
### Passo a passo da instalação e configuração do Redis em um ambiente distribuído utilizando máquinas virtuais pelo sistema operacional Linux feitas para a implementação e utilização do código:

*Passos a serem realizados em ambas as máquinas virtuais, 1 e 2:*
*1. Comandos para a instalação e configuração do Redis utilizando o terminal:*
   - `sudo apt update` : atualiza o sistema através do terminal do linux;
   
   - `sudo apt install redis-server` : instala o Redis;
   
   - `sudo systemctl status redis-server` : verifica se o Redis foi instalado corretamente e se está funcionando corretamente; 
      *Obs.:* Caso esteja, aparecerá a mensagem informando que Redis está ativo.

   -    `sudo nano /etc/redis/redis.conf` : abre o arquivo que contém os dados do Redis, para verificar e editar o que for preciso de modo que funcione corretamente a comunicação entre as máquinas virtuais;
         Dentro desse arquivo, adicione `bind 0.0.0.0`. Isso faz com que Redis aceite todos os tipos de conexões;
         Verifique se o parâmetro *protected-mode* está definido como *protected-mode no* para que seja permitido conexões externas. Caso não esteja, altere deixando como `protected-mode no`;

   - `sudo systemctl restart redis-server` : reinicia o sistema Redis para atualizar as modificações feitas.
   

*A linguagem de programação utilizada é Python. Dentro do terminal, utilizou-se Python3*
*2.  Comandos para instalação e verificação da linguagem de programação Python:*

- `python3 - -version` : verifica se o Python está instalado. Caso não esteja, utilize `sudo apt install python3` para instalar;
- `pip3 --version` : verifica se o gerenciador de pacotes do Python “pip” está instalado. Se não estiver, instale com o comando `sudo apt install python3-pip`


*3. Comandos para configuração e análise de informações a respeito da rede como o IP das máquinas, para que elas se comuniquem corretamente*
- `ifconfig ou ip addr show` : verifica o endereço de rede da máquina virtual. Com isso, verifique se as máquinas virtuais estão conectadas na mesma rede virtual, analisando se o IP e a máscara de sub-rede são parecidos.
   Ex: IP:10.1.1.5 e 10.1.1.6
        Máscara de sub-rede: 255.255.255.0 e 255.255.255.0

- Máquina virtual 1: `ping <endereço da máquina virtual 2>` Máquina virtual 2: `ping <endereço da máquina virtual 1>` 
   Verifica se uma máquina virtual está conectada a outra;
Caso receba mensagens sequenciais de ping, como por exemplo:
  PING 192.168.3.33 (192.168.3.33) 56(84) bytes of data.
  64 bytes from 192.168.3.33: icmp_seq=1 ttl=64 time=0.771 ms
  64 bytes from 192.168.3.33: icmp_seq=2 ttl=64 time=0.560 ms
  64 bytes from 192.168.3.33: icmp_seq=3 ttl=64 time=1.08 ms
significa que está funcionando;

*Após isso, Redis estará configurado em ambas as máquinas virtuais, estando aptas a comunicarem uma com a outra.*
