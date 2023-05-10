import random
from nonebot import on_message, get_driver
from nonebot.adapters import Event
from nonebot.plugin import PluginMetadata
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="通括膨胀",
    description="让你的机器人随机发括号",
    usage="[请查阅插件介绍文档]",
    config=Config
)

global_config = get_driver().config
parsed_config = Config.parse_obj(global_config)

obr = on_message(priority=25, block=False)


@obr.handle()
async def make_lbracket(event: Event):
    msg = event.get_message().extract_plain_text()
    
    if len(msg) < 1:
        return None
    
    last = msg[-1]
    if parsed_config.overbracket_nohalfsize and last in "([{":
        text = "半角异端！"
        chance = parsed_config.overbracket_purpose_chance
    elif last in parsed_config.overbracket_brackets:
        text = last
        chance = parsed_config.overbracket_purpose_chance
    else:
        text = random.choice(parsed_config.overbracket_brackets)
        chance = parsed_config.overbracket_base_chance

    assert 0 <= chance <= 1, "存在错误的概率数值，正确范围为 0~1 之间（包含两端）"

    if random.random() < chance:
        await obr.finish(text)