import requests

def get_eth_block_number():
    """
    Получает текущий номер блока с Etherscan API и возвращает его как целое число.
    """
    try:
        response = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken")
        response.raise_for_status()  # Проверка на ошибки HTTP
        return int(response.json()['result'], 16)
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        raise
    except KeyError:
        print("Failed to find 'result' in response")
        raise
    except ValueError:
        print("Failed to convert block number from hex")
        raise

def get_blockcypher_height():
    """
    Получает текущий высотный блок с BlockCypher API и возвращает его.
    """
    try:
        response = requests.get("https://api.blockcypher.com/v1/eth/main")
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()['height']
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        raise
    except KeyError:
        print("Failed to find 'height' in response")
        raise

def compare_block_numbers():
    """
    Сравнивает номера блоков из Etherscan и BlockCypher.
    """
    try:
        eth_block_number = get_eth_block_number()
        blockcypher_height = get_blockcypher_height()
        
        if eth_block_number == blockcypher_height:
            print("Block numbers match!")
        else:
            print(f"Block numbers do not match: {eth_block_number} (Etherscan) != {blockcypher_height} (BlockCypher)")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    compare_block_numbers()
