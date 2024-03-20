from docx import Document
from docx2pdf import convert
import os

def Edit_Save_PDF(
    arquivo,
    titulo001,
    titulo002,
    dado003,
    dado004,
    dado005,
    dado006,
    dado007,
    dado008,
    dado009,
    data1,
    data2,
    dadobloco,
    condominio_nome,
    motivo,
    unidade,
    nome,
    dia,
    mes,
    morador,
returns,
    datapresente,
    mespresente,
    bloco_unid,
):
    
#________________________________________________SUBSTITUIÇÃO_DE_TERMOS_________________________________________________
    doc = Document(arquivo)
    for p in doc.paragraphs:
        # SUBSTITUIR TITULO 001
        if titulo001 in p.text:
            for run in p.runs:
                if titulo001 in run.text:
                    texto_formatado = run.text.replace(titulo001, condominio_nome)
                    run.text = texto_formatado
        # SUBSTITUIR TITULO 002
        if titulo002 in p.text:
            for run in p.runs:
                if titulo002 in run.text:
                    texto_formatado = run.text.replace(titulo002, condominio_nome)
                    run.text = texto_formatado
        # ENTRADA OU SAIDA 003
        if dado003 in p.text:
            for run in p.runs:
                if dado003 in run.text:
                    texto_formatado = run.text.replace(dado003, motivo)
                    run.text = texto_formatado
        # UNIDADE 004
        if dado004 in p.text:
            for run in p.runs:
                if dado004 in run.text:
                    texto_formatado = run.text.replace(dado004, unidade)
                    run.text = texto_formatado
        # NOME DO CLIENTE 005
        if dado005 in p.text:
            for run in p.runs:
                if dado005 in run.text:
                    texto_formatado = run.text.replace(dado005, nome)
                    run.text = texto_formatado
        # DIA DA MUDANÇA 006
        if dado006 in p.text:
            for run in p.runs:
                if dado006 in run.text:
                    texto_formatado = run.text.replace(dado006, dia)
                    run.text = texto_formatado
        # MES DA MUDANÇA 007
        if dado007 in p.text:
            for run in p.runs:
                if dado007 in run.text:
                    texto_formatado = run.text.replace(dado007, mes)
                    run.text = texto_formatado
        # MORADOR (INQUILINO OU PROPRIETARIO) 008
        if dado008 in p.text:
            for run in p.runs:
                if dado008 in run.text:
                    texto_formatado = run.text.replace(dado008, morador)
                    run.text = texto_formatado
        # REGRAS 009
        if dado009 in p.text:
            for run in p.runs:
                if dado009 in run.text:
                    texto_formatado = run.text.replace(dado009,returns)
                    run.text = texto_formatado
        # DIA DE CRIAÇÃO DO DOCUMENTO 00010
        if data1 in p.text:
            for run in p.runs:
                if data1 in run.text:
                    texto_formatado = run.text.replace(data1, datapresente)
                    run.text = texto_formatado
        # MES DE CRIAÇÃO DO DOCUMENTO 00011
        if data2 in p.text:
            for run in p.runs:
                if data2 in run.text:
                    texto_formatado = run.text.replace(data2, mespresente)
                    run.text = texto_formatado
        # BLOCO
        if dadobloco in p.text:
            for run in p.runs:
                if dadobloco in run.text:
                    if bloco_unid == "0":
                        bloco_unid = ""
                        texto_formatado = run.text.replace(dadobloco, "")
                        run.text = texto_formatado
                    else:
                        texto_formatado = run.text.replace(
                            dadobloco, "Bloco " + bloco_unid
                        )
                        run.text = texto_formatado
                        
#_______________________________DIRETORIOS_SALVAMENTO_ARQUIVO_PDF________________________________________________________________________________________
    if condominio_nome == "Reserva Sul Resort": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Reserva Sul.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    elif condominio_nome == "Jardim Paulista": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Jardim Paulista.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
        
    elif condominio_nome == "Edificio Damasco": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Damasco.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    
    elif condominio_nome == "Edificio Ecoville": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Ecoville.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Edificio Alleanza D'oro": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Alleanza.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Edificio Figueira": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Figueira.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Edificio Itaporai": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Itaporai.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Edificio Marcela e Monica": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Marcela e Monica.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    elif condominio_nome == "Edificio Oliveira": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Oliveira.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Haras Country Village": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Haras.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    elif condominio_nome == "Edificio Prime Office": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Prime Office.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Portal dos Pinheiros": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Portal dos Pinheiros.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Recreio Panorama": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Panorama.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Recreio Humaita":
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Humaita.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    elif condominio_nome == "Valencia Turia": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Turia.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    elif condominio_nome == "Santa Angela": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Santa Angela.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Santa Helena": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Santa Helena.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Santa Monica 1": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Santa Monica 1.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Santa Monica 2": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Santa Monica 2.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Villa Florença": 
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Villa Florença.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        

    elif condominio_nome == "Vivendas do Sul":  
        arquivo_diretorio = open(r"C:\\Editor de Autorizações\\Diretorios\\Vivendas do Sul.txt", encoding="utf-8")
        diretorio_str = arquivo_diretorio.read()
        doc.save(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        convert(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx", diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".pdf")
        os.remove(diretorio_str + " " + str(bloco_unid) + " " + str(unidade) + " "  + str(motivo) + " " + str(condominio_nome) + ".docx")
        
    else: print("Diretorio Invalido :)")