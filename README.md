## This Code is old and at times awful.
## Wouldn't recommend actually trying to use the bot.
## Oh the official bot is also offline.


This is Management bot for telegram. You can find him in telegram as @LoopedInfinity (Loop).

The configuration is easy. Just look at the basic __main.py__ file.

The modules are in .modules. You can add new modules if you want. After you code your next module you need to import the function and create handlers in __main__.py. You can do that that way:

```
# newmodule.py:

def NewFunction(bot, update):
  # your function
  
```

```
# __main__.py
from modules.newmodule import NewFunction
```

You can create the handler like the other ones in the file.
 
 
The configuration process is simplified as much as possible.

You need to add your api token to that line:

```
API = "HERE YOUR TOKEN" # API Token
```
