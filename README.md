# xagpy

Api wrapper for the Xag(Xbox account generator) api

---

## How to use

1. Get a api key from this [discord server](https://discord.gg/Ytbnqh2PvM)

### Example code

> Get current coins in balance

```py
from xagpy import xagpy

token = ""
xagpy = xagpy(token)
coins = xagpy.get_coins()
print("Coins:", coins)
```
