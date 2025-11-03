from funcoes_auxiliares.funcs_auxiliares import ler_cargas
from funcoes_auxiliares.status_aparelhos import infos
import json
import os
from dotenv import load_dotenv

import tinytuya
import time

TOMADA_DEVICE_ID = "INSIRA SUAS INFORMAÇÕES AQUI"
TOMADA_IP_ADDRESS = "INSIRA SUAS INFORMAÇÕES AQUI" 
TOMADA_LOCAL_KEY = "INSIRA SUAS INFORMAÇÕES AQUI"

load_dotenv()
caminho_status = os.getenv("CARGAS")

CONSUMO_PADRAO = {
    "Computador": 150,
    "Geladeira": 300,
    "Televisão": 175,
    "Ar Condicionado": 1200,
    "Air Fryer": 1500,
    "Ventilador": 70,
    "Lâmpada LED": 10,
    "Cafeteira": 800
}

CLOUD = tinytuya.Cloud(
    apiRegion="INSIRA SUAS INFORMAÇÕES AQUI", 
    apiKey="INSIRA SUAS INFORMAÇÕES AQUI",
    apiSecret="INSIRA SUAS INFORMAÇÕES AQUI",
    apiDeviceID="INSIRA SUAS INFORMAÇÕES AQUI"  
)

DEVICE_ID = "INSIRA SUAS INFORMAÇÕES AQUI"


def get_consumo_tomada_inteligente():
    try:
        result = CLOUD.getstatus(DEVICE_ID)
        if not result.get("success"):
            print(" Falha ao obter dados da tomada Tuya Cloud")
            return {"potencia": 0, "estado": False}


        dados = {item["code"]: item["value"] for item in result["result"]}

        potencia_watts = float(dados.get("cur_power", 0)) / 10.0  
        estado_tomada = bool(dados.get("switch_1", False))

        print(f"⚡ Potência: {potencia_watts:.1f} W | Estado: {'Ligada' if estado_tomada else 'Desligada'}")
        return {"potencia": potencia_watts, "estado": estado_tomada}

    except Exception as e:
        print(f"ERRO Tuya Cloud - get_consumo_tomada_inteligente(): {e}")
        return {"potencia": 0, "estado": False}


def controlar_tomada(estado: bool):
    try:
        comando = {"commands": [{"code": "switch_1", "value": estado}]}
        res = CLOUD.sendcommand(DEVICE_ID, comando)
        if res.get("success"):
            print(f" Tomada {'ligada' if estado else 'desligada'} com sucesso!")
            return True
        else:
            print(f"⚠️ Falha ao mudar estado da tomada: {res}")
            return False
    except Exception as e:
        print(f"ERRO Tuya Cloud - controlar_tomada(): {e}")
        return False

def ligar_cargas_prioritarias():
    try:
        with open(caminho_status, 'r') as f:
            status = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        status = {"cargas_prioritarias_ativas": False}
    
    controlar_tomada(True) # Envia comando para ligar

    status['cargas_prioritarias_ativas'] = True
    with open(caminho_status, 'w') as f:
        json.dump(status, f, indent=2)
    return status

def desligar_cargas_prioritarias():
    with open(caminho_status, 'r+') as f:
        status = json.load(f)
        status['cargas_prioritarias_ativas'] = False
        f.seek(0)
        json.dump(status, f, indent=2)

    controlar_tomada(False) # Envia comando para desligar

def verificar_status_cargas():
    try:
        with open(caminho_status, 'r') as f:
            status = json.load(f)
            return status.get('cargas_prioritarias_ativas', False)
    except FileNotFoundError:
        return False



def consumo_aparelhos():
    if not verificar_status_cargas():
        return {'Cargas prioritárias desligadas.'}
    else:
        cargas_prioritarias = ler_cargas()
        consumo_individual = {}
        consumo_total_cargas = 0

        for nome_aparelho in cargas_prioritarias.values():
            consumo_w = 0

            if nome_aparelho == "Tomada inteligente":
                dados_tomada = get_consumo_tomada_inteligente()
                consumo_w = dados_tomada.get("potencia", 0)
            else:
                consumo_w = CONSUMO_PADRAO.get(nome_aparelho, 0)

            consumo_individual[f'Consumo {nome_aparelho}'] = f'{consumo_w:.1f}'
            consumo_total_cargas += consumo_w

        return {
            'consumo_de_cada_aparelho': consumo_individual,
            'consumo_total_das_cargas': consumo_total_cargas
        }

def info_consumo():
    if not verificar_status_cargas():
        return {'duracao': 'Cargas prioritárias desligadas.'}
    else:
        dados_consumo = consumo_aparelhos()
        consumo_cargas = dados_consumo.get('consumo_total_das_cargas', 0)

        infos_aparelhos = infos()
        bateria_valor = int(infos_aparelhos["bateria_carga"].replace("%", ""))
        bateria_valor = bateria_valor/100

        if consumo_cargas == 0:
            return {'duracao': 'Sem consumo, a bateria dura indefinidamente.'}

        # Capacidade de Armazenamento nominal da bateria: 5400 Wh
        duracao_bateria = 5400 * bateria_valor / consumo_cargas
        
        return {'duracao': f'Caso acabe a luz, sua bateria conseguirá abastecer suas cargas por {int(duracao_bateria)}h.'}