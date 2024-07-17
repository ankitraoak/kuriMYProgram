<p align="center">
    <a href="https://github.com/kurimypyrogram/kurimypyrogram">
        <img src="https://docs.kurimypyrogram.org/_static/kurimypyrogram.png" alt="kurimypyrogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://kurimypyrogram.org">
        Homepage
    </a>
    •
    <a href="https://docs.kurimypyrogram.org">
        Documentation
    </a>
    •
    <a href="https://docs.kurimypyrogram.org/releases">
        Releases
    </a>
    •
    <a href="https://t.me/kurimypyrogram">
        News
    </a>
</p>

## kurimypyrogram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

``` python
from kurimypyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from kurimypyrogram!")


app.run()
```

**kurimypyrogram** is a modern, elegant and asynchronous [MTProto API](https://docs.kurimypyrogram.org/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

If you'd like to support kurimypyrogram, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/delivrance).
- [Become a LiberaPay patron](https://liberapay.com/delivrance).
- [Become an OpenCollective backer](https://opencollective.com/kurimypyrogram).

### Key Features

- **Ready**: Install kurimypyrogram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/kurimypyrogram/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install kurimypyrogram
```

### Resources

- Check out the docs at https://docs.kurimypyrogram.org to learn more about kurimypyrogram, get started right
away and discover more in-depth material for building your client applications.
- Join the official channel at https://t.me/kurimypyrogram and stay tuned for news, updates and announcements.
