# backend/schemas.py
from pydantic import BaseModel, Field

class TextInput(BaseModel):
    message: str = Field(..., description="Texto da mensagem a ser analisada")

class TextOutput(BaseModel):
    risk: str = Field(..., description="Classificação da IA (ex: 'high', 'low')")
    confidence: float = Field(..., ge=0, le=1, description="Nível de confiança (0 a 1)")
    reason: str = Field(..., description="Motivo gerado pela IA para a classificação")
    risk_percentage: float = Field(..., ge=0, le=100, description="Percentual de risco estimado")
    indicators: list = Field(default=[], description="Indicadores de risco encontrados")
