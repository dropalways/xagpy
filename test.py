from xagpy import xagpy

api_token = ""

xagpy = xagpy(api_token)


def main():

  # Test generate_account() method
  # print("Testing generate_account():")
  # print("Generating account without test mode:")
  # account_data = xagpy.generate_account()
  # print("Generated Account:", account_data)

    print("Testing get_coins():")
    coins = xagpy.get_coins()
    print("Coins:", coins)

    print("Testing generate_account():")
    test_account_data = xagpy.generate_account(test_mode=True)
    print("Generated Test Account:", test_account_data)

    print("\nTesting get_stock():")
    stock_data = xagpy.get_stock()
    print("Stock Data:", stock_data)


if __name__ == "__main__":
    main()
