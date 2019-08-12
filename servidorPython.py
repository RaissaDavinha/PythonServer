#!/usr/bin/env python
import logging
import socket
import sys

### passos ###
#1 - receber solicitacao do cliente
#2 - gerar arquivo para enviar (config, status ou shapefile)
#   - considerar a existencia de mais de um arquivo de configuracao
#3 - enviar arquivo
#4 - se receber arquivo de configuracao, atualizar valores no arquivo .ini


def initialize():
        HOST = ''              # Endereco IP do Servidor
        PORT = 5075            # Porta que o Servidor esta

        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.SOCK_DGRAM
        orig = (HOST, PORT)
        udp.bind(orig)

        logger = logging.getLogger('serverLog')
        file_log_handler = logging.FileHandler('/home/linaro/SensorVision/serverLog.log')

        logger.addHandler(file_log_handler)
        stderr_log_handler = logging.StreamHandler()

        logger.addHandler(stderr_log_handler)
        logger.setLevel('DEBUG')

        # nice output format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log_handler.setFormatter(formatter)
        stderr_log_handler.setFormatter(formatter)

        logger.debug('Servidor inicializado')

        #portas diferentes vao enviar e receber dados para evitar perdas por cruzamento
        while True:
                mesg,cliente = udp.recvfrom(1024)
                logger.debug('Concetado por %s', cliente)

                dataDecode = mesg.decode("utf-8")

                if dataDecode.find('default') != -1:
                        logger.debug('Recebi pedido de default')
                        my_file=open(r"/home/linaro/SensorVision/servidor/default.json","r")
                        file_encoded = my_file.read().encode()
                        my_file.close()
                        udp.sendto (file_encoded,(cliente[0],6075))

                if dataDecode.find('status') != -1:
                        my_file=open(r"/home/linaro/SensorVision/servidor/status.json","r")
                        file_encoded = my_file.read().encode()
                        my_file.close()
                        logger.debug('Recebi pedido de status')
                        udp.sendto (file_encoded,(cliente[0],6075))
						
                if dataDecode.find('shapefile') != -1:
                        my_file=open(r"/home/linaro/SensorVision/servidor/doc.kml","r")
                        file_encoded = my_file.read().encode()
                        my_file.close()
                        logger.debug('Recebi pedido de shapefile')
                        udp.sendto (file_encoded,(cliente[0],6075))
						
                if dataDecode.find('controle') != -1:
                        with open(r"/home/linaro/SensorVision/default.json", "a") as the_file:
                                        the_file.seek(0)
                                        the_file.truncate()
                                        the_file.write(dataDecode)
                                        logger.debug('Recebi configuracao: %s', dataDecode)
                                        logger.debug('Salvei em arquivo')
                                        print("Salvei")
        udp.close()

#funcao gerar config json
#controle:0
#abrir arquivo .ini
#apenas colocar variaveis definidas previamente e somente numericas


#funcao atualizar arquivo de configuracao
#salvar dados recebidos como json
#pelo nome das variaveis de configuracao pre-definidas, substituir os valores da mesma atraves da ordem das variaveis, ou comparando os nomes

if __name__ == "__main__":
    initialize()
