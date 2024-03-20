def Horarios (condominio):
     
    if condominio == "Reserva Sul Resort":
        return "24.1). As mudanças, bem como cargas, descargas e entregas de mercadorias, móveis e similares. Somente poderão ser realizadas, entre o período das 8:00h as 17:00h, de segunda a sexta-feira, e, aos sábados, das 8:00h as 15:00h, exceto feriados."
    elif condominio in ["Edificio Damasco","Edificio Oliveira","Edificio Figueira","Edificio Ecoville","Humaita","Edificio Itaporai","Edificio Marcela e Monica","Panorama","Santa Angela","Santa Helena","Santa Monica 1","Villa Florença"]:
        return "Favor entrar em contato com o zelador para verificação de data e horário. (o regulamento estipula mudanças entre segundas-feiras a sextas-feiras das 8h às 17h)." 
    elif condominio in ["Edificio Alleanza D'oro","Vivendas do Sul"]:
     return "Favor entrar em contato com o zelador para verificação de data e horário. (o regulamento estipula mudanças de segunda-feira à sexta-feira das 8:00h às 17:00h e aos Sábados das 8:00h às 12:00h)."  
    elif condominio in ["Haras Country Village","Jardim Paulista"]:
     return "Favor entrar em contato com o zelador para verificação de data e horário. (o regulamento estipula mudanças entre segundas-feiras à sextas-feiras das 8h às 17h e aos sábados das 8h às 15h)."  
    elif condominio in ["Portal dos Pinheiros"]:
     return "Favor entrar em contato com o zelador para verificação de data e horário. (o regulamento estipula mudanças entre segundas-feiras a sextas-feiras das 8h às 18h e aos sábados das 8h às 17h)."   
    elif condominio in ["Edificio Prime Office"]:
     return "Favor entrar em contato com o zelador para verificação de data e horário. (os horários para mudanças são de segundas – feiras as sextas - feiras das 09h00 às 11h30 ou das 14h00 às 17h30)."   
    elif condominio in ["Valencia Turia"]:
        return "Favor entrar em contato com o zelador para verificação de data e horário. (o regulamento estipula mudanças entre segundas-feiras a sextas-feiras das 8h às 18h e aos sábados das 8h às 15h)."  
    elif condominio in ["Santa Monica 2"]:
        return "Favor entrar em contato com o zelador para verificação de data e horário. (o regulamento estipula mudanças entre segundas-feiras à sábados das 7:30h às 18h)"
    else:  return "SEM CONDOMINIO"  
