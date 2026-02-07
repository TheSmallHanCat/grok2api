"""
Grok 模型管理服务
"""

from enum import Enum
from typing import Optional, Tuple, List
from pydantic import BaseModel, Field

from app.core.exceptions import ValidationException


class Tier(str, Enum):
    """模型档位"""

    BASIC = "basic"
    SUPER = "super"


class Cost(str, Enum):
    """计费类型"""

    LOW = "low"
    HIGH = "high"


class ModelInfo(BaseModel):
    """模型信息"""

    model_id: str
    grok_model: str
    model_mode: str
    tier: Tier = Field(default=Tier.BASIC)
    cost: Cost = Field(default=Cost.LOW)
    display_name: str
    description: str = ""
    is_video: bool = False
    is_image: bool = False


class ModelService:
    """模型管理服务"""

    MODELS = [
        ModelInfo(
            model_id="grok-3",
            grok_model="grok-3",
            model_mode="MODEL_MODE_GROK_3",
            cost=Cost.LOW,
            display_name="GROK-3",
        ),
        ModelInfo(
            model_id="grok-3-mini",
            grok_model="grok-3",
            model_mode="MODEL_MODE_GROK_3_MINI_THINKING",
            cost=Cost.LOW,
            display_name="GROK-3-MINI",
        ),
        ModelInfo(
            model_id="grok-3-thinking",
            grok_model="grok-3",
            model_mode="MODEL_MODE_GROK_3_THINKING",
            cost=Cost.LOW,
            display_name="GROK-3-THINKING",
        ),
        ModelInfo(
            model_id="grok-4",
            grok_model="grok-4",
            model_mode="MODEL_MODE_GROK_4",
            cost=Cost.LOW,
            display_name="GROK-4",
        ),
        ModelInfo(
            model_id="grok-4-mini",
            grok_model="grok-4-mini",
            model_mode="MODEL_MODE_GROK_4_MINI_THINKING",
            cost=Cost.LOW,
            display_name="GROK-4-MINI",
        ),
        ModelInfo(
            model_id="grok-4-thinking",
            grok_model="grok-4",
            model_mode="MODEL_MODE_GROK_4_THINKING",
            cost=Cost.LOW,
            display_name="GROK-4-THINKING",
        ),
        ModelInfo(
            model_id="grok-4-heavy",
            grok_model="grok-4",
            model_mode="MODEL_MODE_HEAVY",
            cost=Cost.HIGH,
            tier=Tier.SUPER,
            display_name="GROK-4-HEAVY",
        ),
        ModelInfo(
            model_id="grok-4.1-mini",
            grok_model="grok-4-1-thinking-1129",
            model_mode="MODEL_MODE_GROK_4_1_MINI_THINKING",
            cost=Cost.LOW,
            display_name="GROK-4.1-MINI",
        ),
        ModelInfo(
            model_id="grok-4.1-fast",
            grok_model="grok-4-1-thinking-1129",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.LOW,
            display_name="GROK-4.1-FAST",
        ),
        ModelInfo(
            model_id="grok-4.1-expert",
            grok_model="grok-4-1-thinking-1129",
            model_mode="MODEL_MODE_EXPERT",
            cost=Cost.HIGH,
            display_name="GROK-4.1-EXPERT",
        ),
        ModelInfo(
            model_id="grok-4.1-thinking",
            grok_model="grok-4-1-thinking-1129",
            model_mode="MODEL_MODE_GROK_4_1_THINKING",
            cost=Cost.HIGH,
            display_name="GROK-4.1-THINKING",
        ),
        ModelInfo(
            model_id="grok-imagine-1.0",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Image",
            description="Image generation model",
            is_image=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-edit",
            grok_model="imagine-image-edit",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Image Edit",
            description="Image edit model",
            is_image=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video",
            description="Video generation model",
            is_video=True,
        ),
        # Portrait 纵向视频模型
        ModelInfo(
            model_id="grok-imagine-1.0-video-portrait-6s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Portrait 6s",
            description="Video generation model (9:16, 6s, 720p)",
            is_video=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video-portrait-10s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Portrait 10s",
            description="Video generation model (9:16, 10s, 720p)",
            is_video=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video-portrait-12s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Portrait 12s",
            description="Video generation model (9:16, 12s, 720p)",
            is_video=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video-portrait-15s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Portrait 15s",
            description="Video generation model (9:16, 15s, 720p)",
            is_video=True,
        ),
        # Landscape 横向视频模型
        ModelInfo(
            model_id="grok-imagine-1.0-video-landscape-6s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Landscape 6s",
            description="Video generation model (16:9, 6s, 720p)",
            is_video=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video-landscape-10s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Landscape 10s",
            description="Video generation model (16:9, 10s, 720p)",
            is_video=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video-landscape-12s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Landscape 12s",
            description="Video generation model (16:9, 12s, 720p)",
            is_video=True,
        ),
        ModelInfo(
            model_id="grok-imagine-1.0-video-landscape-15s",
            grok_model="grok-3",
            model_mode="MODEL_MODE_FAST",
            cost=Cost.HIGH,
            display_name="Grok Video Landscape 15s",
            description="Video generation model (16:9, 15s, 720p)",
            is_video=True,
        ),
    ]

    _map = {m.model_id: m for m in MODELS}

    @classmethod
    def get(cls, model_id: str) -> Optional[ModelInfo]:
        """获取模型信息"""
        return cls._map.get(model_id)

    @classmethod
    def list(cls) -> list[ModelInfo]:
        """获取所有模型"""
        return list(cls._map.values())

    @classmethod
    def valid(cls, model_id: str) -> bool:
        """模型是否有效"""
        return model_id in cls._map

    @classmethod
    def to_grok(cls, model_id: str) -> Tuple[str, str]:
        """转换为 Grok 参数"""
        model = cls.get(model_id)
        if not model:
            raise ValidationException(f"Invalid model ID: {model_id}")
        return model.grok_model, model.model_mode

    @classmethod
    def pool_for_model(cls, model_id: str) -> str:
        """根据模型选择 Token 池"""
        model = cls.get(model_id)
        if model and model.tier == Tier.SUPER:
            return "ssoSuper"
        return "ssoBasic"

    @classmethod
    def pool_candidates_for_model(cls, model_id: str) -> List[str]:
        """按优先级返回可用 Token 池列表"""
        model = cls.get(model_id)
        if model and model.tier == Tier.SUPER:
            return ["ssoSuper"]
        # 基础模型优先使用 basic 池，缺失时可回退到 super 池
        return ["ssoBasic", "ssoSuper"]

    @classmethod
    def parse_video_params(cls, model_id: str) -> Tuple[str, int, str]:
        """
        从模型名称解析视频参数

        Args:
            model_id: 模型 ID

        Returns:
            Tuple[aspect_ratio, video_length, resolution_name]

        Examples:
            grok-imagine-1.0-video-portrait-6s -> ("9:16", 6, "720p")
            grok-imagine-1.0-video-portrait-10s -> ("9:16", 10, "720p")
            grok-imagine-1.0-video-landscape-12s -> ("16:9", 12, "720p")
            grok-imagine-1.0-video-landscape-15s -> ("16:9", 15, "720p")
            grok-imagine-1.0-video -> ("3:2", 6, "720p")  # 默认值
        """
        # 默认参数
        aspect_ratio = "3:2"
        video_length = 6
        resolution_name = "720p"

        # 解析模型名称
        if "portrait" in model_id:
            aspect_ratio = "9:16"
        elif "landscape" in model_id:
            aspect_ratio = "16:9"

        if "6s" in model_id:
            video_length = 6
        elif "10s" in model_id:
            video_length = 10
        elif "12s" in model_id:
            video_length = 12
        elif "15s" in model_id:
            video_length = 15

        return aspect_ratio, video_length, resolution_name


__all__ = ["ModelService"]
