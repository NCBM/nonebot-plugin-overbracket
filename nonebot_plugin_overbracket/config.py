from pydantic import BaseModel


class Config(BaseModel, extra="ignore"):
    """Plugin Config Here"""

    overbracket_base_chance: float = 0.12
    """收到任意消息时发送括号的概率"""

    overbracket_purpose_chance: float = 0.42
    """收到末尾带括号消息时发送括号的概率"""

    overbracket_brackets: str = "（"
    """用于检测与发送的括号备选列表"""

    overbracket_nohalfsize: bool = True
    """在消息文本末尾为半角括号时是否以同等概率发送“半角异端！”"""