def lightspeed(speedMPH):
    if speedMPH>20:
        print('shift to gerar 1')
    elif speedMPH>30:
        print('shift to gear 2')
    elif speedMPH>40:
        print('shift to gear 3')
    elif speedMPH>70:
        print('return to gear 1')
    else:
        print('nice driving')
lightspeed(80)