import asyncio
import websockets
import time
import json
from func import funciones

async def get_data():
    uri = "ws://209.126.82.146:8080"
    async with websockets.connect(uri) as websocket:
        data = []
        while True:      
            while len(data) <= 100:
                await websocket.send("señal")
                respuesta = await websocket.recv()           
                data.append(respuesta)
            b_values = []
            numeros_pares = []
            numeros_impares = []
            numeros_primos = []
            for i in data:
                json_data = json.loads(i)  
                b_values.append(json_data["b"])

            info = {
            "_max_number" : funciones.max_num(b_values),
            "min_number" : funciones.min_num(b_values),
            "first_number" : funciones.first_number(b_values),
            "last_number" : funciones.last_number(b_values),
            "number_of_prime_numbers" :  funciones.number_of_prime_numbers(b_values),
            "number_of_even_numbers" : funciones.number_of_even_numbers(b_values),
            "number_of_odd_numbers" : funciones.number_of_odd_numbers(b_values)
            }            
            b_values.clear()   
            data.clear()
            numeros_pares.clear()
            numeros_impares.clear()
            numeros_primos.clear()
            for item in info.items():
                print(item)
            time.sleep(60)

if __name__ == "__main__":       
    asyncio.get_event_loop().run_until_complete(get_data())