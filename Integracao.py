from os import getcwd, listdir
import os
import re
import shutil
import time
while True:
    print("=====================MENU===================")
    n=str(input("[1]Renomear arquivos\n[2]Criar Pastas e Mover arquivos\n[0]Sair\n============================================"))
 
    if n == "1":#MENU DE RENOMEAR
        dia=int(input("Nª do dia do Relatorio: "))
        mes=int(input("Nª do mês do Relatorio: "))
        
        #===========================Leitura de arquivos na pasta =============================
        print(getcwd())
        doc=[]
        for c in listdir():
            doc.append(c)
        qt = len(doc)
        #=============================== Leitura de conteudo para poder renomear=====================
        #REDE FIBERLINK
        for i in range (qt):
            if doc[i].find('fiberlink-IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('fiberlink-IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('fiberlink-GGC') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_ggc_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('fiberlink-NFX') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_nfx_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('fiberlink-FNA') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_fna_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('fiberlink-CDN-Fanweb') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_cdn_fwb_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('fiberlink-ix-IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_ix-ora_rede-fiberlink_{}-0{}-2021.pdf".format(dia,mes))      
            if doc[i].find('fiberlink-ix-IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link_ipv6_ix-ora_rede-fiberlink_{}0{}-2021.pdf".format(dia,mes))
        #REDE INFOWEB
            if doc[i].find('infoweb_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb_GGCI') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_ggc_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb_ggcII') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_ggc02_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb_NFX') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_nfx_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb_FNA') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_cdn_fna_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb_ix_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_ix-ora_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb-_ix_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_ix-ora_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb-TSA_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_ix_tsa_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb-TSA_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_ix_tsa_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb-SLZ_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_ix_slz_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('infoweb-SLZ_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_ix_slz_rede-infoweb_{}-0{}-2021.pdf".format(dia,mes))
        #REDE ITECH
            if doc[i].find('itech_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_ipv4_amarante') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_rede-itech-amarante_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_ipv6_amarante') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-itech-amarante_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_GGC') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-v6-cdn-ggc_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_NFX') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-v6-cdn-nfx_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_FNA') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-v6-cdn-fna_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_ix_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_ix_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_ix-ora_rede-itech_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_ix_Amarante_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6-ix-amarante_rede-itech{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('itech_ix_Amarante_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar, "relatorio_link-ipv4-ix-ora-amarante_rede-itech{}-0{}-2021.pdf".format(dia,mes))   

        #REDE MEGAVIA
            if doc[i].find('megavia_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_v6_rede-megavia_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('megavia_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-megavia_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('megavia_ix_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-megavia-{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('megavia_ix_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6-ix-ora_rede-megavia-{}-0{}-2021.pdf".format(dia,mes))

        #REDE iNTERATIVA TSA  
            if doc[i].find('interativa_tsa_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_rede-interativa-tsa_s{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_tsa_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-interativa-tsa_s{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_tsa_GGC') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-v6-cdn-ggc_rede-interativa-tsa_s{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_tsa_NFX') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-v6-cdn-nfx_rede-interativa-tsa_s{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_tsa_ix_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-interativa-tsa_s{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_tsa_ix_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6-ix-ora_rede-interativa-tsa_s{}-0{}-2021.pdf".format(dia,mes))
        #REDE INTERATIVA PIP
            if doc[i].find('interativa_pip_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_pip_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-interativa-pip_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_pip_ix_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('interativa_pip_ix_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(dia,mes))
        #REDE COMPUNET
            if doc[i].find('compunet_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4_rede-compunet_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('compunet_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6_rede-compunet_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('compunet_CDN_IPV4') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv4-cdn_rede-compunet_{}-0{}-2021.pdf".format(dia,mes))

            if doc[i].find('compunet_CDN_IPV6') >=0:
                procurar = doc[i]
                os.rename(procurar,"relatorio_link-ipv6-cdn_rede-compunet_{}-0{}-2021.pdf".format(dia,mes))
        print(" Renomeação concluida com sucesso")


    if n =="2":#Menu de mover e criar pastas
        #====================== Criar pastas ===============================================
        diretorios = os.listdir(os.curdir)
        os.mkdir(f"./rede-megavia")
        os.mkdir(f"./rede-itech")
        os.mkdir(f"./rede-interativa-tsa")
        os.mkdir(f"./rede-interativa-pip")
        os.mkdir(f"./rede-infoweb")
        os.mkdir(f"./rede-fiberlink")
        os.mkdir(f"./rede-compunet")
        #===========================Leitura de arquivos na pasta =============================
        print(getcwd())
        doc=[]
        for c in listdir():
            doc.append(c)
        qt = len(doc)
        #=============================== Leitura de conteudo do arquivo para poder utitiliza a expessão regular=====================
        for i in range (qt):
            if doc[i].find('rede-megavia') >=0:
                procurar = doc[i]
                caminho= './rede-megavia/'
                shutil.move(procurar, caminho)
        for i in range (qt):
            if doc[i].find('rede-itech') >=0:
                procurar = doc[i]
                caminho= './rede-itech'
                shutil.move(procurar, caminho)
        for i in range (qt):
            if doc[i].find('rede-interativa-tsa') >=0:
                procurar = doc[i]
                caminho= './rede-interativa-tsa'
                shutil.move(procurar, caminho)
        for i in range (qt):
            if doc[i].find('rede-interativa-pip') >=0:
                procurar = doc[i]
                caminho= './rede-interativa-pip'
                shutil.move(procurar, caminho)
        for i in range (qt):
            if doc[i].find('rede-infoweb') >=0:
                procurar = doc[i]
                caminho= './rede-infoweb'
                shutil.move(procurar, caminho)
        for i in range (qt):
            if doc[i].find('rede-fiberlink') >=0:
                procurar = doc[i]
                caminho= './rede-fiberlink'
                shutil.move(procurar, caminho)
        for i in range (qt):
            if doc[i].find('rede-compunet') >=0:
                procurar = doc[i]
                caminho= './rede-compunet'
                shutil.move(procurar, caminho)

    if n == "0":#Menu de Sair 
       break
    if n != "1" and n!="2" and n!="0":#Menu de valores errados
        print("Valor invalido")
        n=str(input("[1]Renomear arquivos\n[2]Criar Pastas e Mover arquivos\n[0]Sair"))
