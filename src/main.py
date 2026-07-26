from machine import Pin, I2C
import time

BOTAO_PIN = 27       
I2C_SDA_PIN = 21
I2C_SCL_PIN = 22
MPU_ADDR = 0x68       

LIMITE_TEMPO_X_MS = 5000     
LIMITE_VARIACAO_Y = 3.0      

INTERVALO_LEITURA_MS = 200   
LOOP_TICK_MS = 50            

MSG_INICIALIZADO = "Sistema de Monitoramento Inicializado"
MSG_ALERTA_PORTA = "ALERTA: Porta aberta por muito tempo!"
MSG_ALERTA_TERMICO = "ALERTA: Degradacao termica detectada!"
MSG_NORMALIZADO = "Status: Sistema Normalizado."
botao = None
i2c = None

porta_aberta = False
inicio_porta_aberta_ms = None
alarme_porta_ativo = False

temp_referencia = None
alarme_termico_ativo = False

sistema_em_alarme = False  


def mpu_wakeup():
    i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')


def ler_temperatura():
    dados = i2c.readfrom_mem(MPU_ADDR, 0x41, 2)
    bruto = (dados[0] << 8) | dados[1]
    if bruto & 0x8000:           
        bruto -= 0x10000
    return (bruto / 340.0) + 36.53


def porta_esta_aberta():

    return botao.value() == 1


# ---------------------------------------------------------------
# ESTADO A: INICIALIZACAO DO SISTEMA
# ---------------------------------------------------------------

def inicializar_sistema():
    global botao, i2c
    global porta_aberta, inicio_porta_aberta_ms, alarme_porta_ativo
    global temp_referencia, alarme_termico_ativo, sistema_em_alarme

    botao = Pin(BOTAO_PIN, Pin.IN, Pin.PULL_UP)
    i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=400000)
    mpu_wakeup()

    porta_aberta = porta_esta_aberta()
    inicio_porta_aberta_ms = time.ticks_ms() if porta_aberta else None
    alarme_porta_ativo = False

    temp_referencia = ler_temperatura()
    alarme_termico_ativo = False

    sistema_em_alarme = False

    print(MSG_INICIALIZADO)


# ---------------------------------------------------------------
# ESTADO B: TEMPO DE PORTA ABERTA (LIMITE X)
# ---------------------------------------------------------------

def avaliar_porta(agora):
    global porta_aberta, inicio_porta_aberta_ms, alarme_porta_ativo

    aberta_agora = porta_esta_aberta()

    if aberta_agora and not porta_aberta:
        # transicao: a porta acabou de abrir -> inicia o cronometro
        inicio_porta_aberta_ms = agora

    if not aberta_agora and porta_aberta:
        # transicao: a porta acabou de fechar -> zera o cronometro/alarme
        inicio_porta_aberta_ms = None
        alarme_porta_ativo = False

    porta_aberta = aberta_agora

    if porta_aberta and inicio_porta_aberta_ms is not None and not alarme_porta_ativo:
        if time.ticks_diff(agora, inicio_porta_aberta_ms) >= LIMITE_TEMPO_X_MS:
            alarme_porta_ativo = True
            print(MSG_ALERTA_PORTA)


# ---------------------------------------------------------------
# ESTADO C: ELEVACAO TERMICA / DEGRADACAO (VARIACAO Y)
# ---------------------------------------------------------------

def avaliar_temperatura():
    global temp_referencia, alarme_termico_ativo

    temp_atual = ler_temperatura()
    delta = temp_atual - temp_referencia

    if delta >= LIMITE_VARIACAO_Y and not alarme_termico_ativo:
        alarme_termico_ativo = True
        print(MSG_ALERTA_TERMICO)
        return  

    if alarme_termico_ativo and delta < LIMITE_VARIACAO_Y:
        alarme_termico_ativo = False
        temp_referencia = temp_atual
        return

    if not alarme_termico_ativo and not porta_aberta:
        temp_referencia = temp_atual


# ---------------------------------------------------------------
# ESTADO D: NORMALIZACAO (SOMENTE QUANDO AMBAS AS CONDICOES ESTAO SEGURAS)
# ---------------------------------------------------------------

def avaliar_normalizacao():
    global sistema_em_alarme

    em_alarme = alarme_porta_ativo or alarme_termico_ativo

    if em_alarme:
        sistema_em_alarme = True
    elif sistema_em_alarme:
        sistema_em_alarme = False
        print(MSG_NORMALIZADO)


# ---------------------------------------------------------------
# LOOP PRINCIPAL (NAO-BLOQUEANTE)
# ---------------------------------------------------------------

def main():
    inicializar_sistema()  
    ultima_leitura = time.ticks_ms()

    while True:
        agora = time.ticks_ms()

        if time.ticks_diff(agora, ultima_leitura) >= INTERVALO_LEITURA_MS:
            ultima_leitura = agora
            avaliar_porta(agora)
            avaliar_temperatura()
            avaliar_normalizacao()

        time.sleep_ms(LOOP_TICK_MS)


if __name__ == "__main__":
    main()