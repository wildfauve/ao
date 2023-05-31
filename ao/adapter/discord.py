from discord_webhook import DiscordWebhook

from ao.util import env


def send(message_text):
    hook = DiscordWebhook(url=_channel_url(), content=message_text)
    hook.execute()
    pass


def _channel_url():
    return env.Env().discord_channel_url()
