from breeze_connect import BreezeConnect

# Initialize SDK
breeze = BreezeConnect(api_key="your-api-key")

# Generate Session
breeze.generate_session(api_secret="your-api-secret",
                        session_token="your-session-token")

# Connect to websocket(it will connect to tick-by-tick data server)
#breeze.ws_connect()

holdings = breeze.get_demat_holdings()
print(holdings)