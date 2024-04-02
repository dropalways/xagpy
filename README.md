# xagpy

Api wrapper for the Xag(Xbox account generator) api

# How to use

1. Get a api key from this [discord server](https://discord.gg/Ytbnqh2PvM)

# Example code

> Get current coins in balance

```py
from xagpy import xagpy

token = ""
xagpy = xagpy(token)
coins = xagpy.get_coins()
print("Coins:", coins)
```

> Generate an account

```py
from xagpy import xagpy

token = ""
xagpy = xagpy(token)
coins = xagpy.generate_account()
print("Generated Account:", coins)
```

> Generate an account in test mode

```py
from xagpy import xagpy

token = ""
xagpy = xagpy(token)
coins = xagpy.generate_account(test_mode=True)
print("Generated Account:", coins)
```

> Get current stock

```py
from xagpy import xagpy

stock = xagpy.get_stock()
print("Stock Data:", stock)
```

# Need any help?

Feel free to contact me on discord(linked in my [github profile](https://github.com/dropalways))
