"""Public reference component for the CMCA-KGC channel-mixing block.

The complete CMCA-KGC architecture is intentionally not included in this
partial release. Community assignments are supplied as external structural
features in the full implementation.
"""

from __future__ import annotations

import torch
from torch import nn
from torch.nn import functional as F


class ChannelMixingBlock(nn.Module):
    """A compact gated channel-mixing block for feature sequences.

    This public component illustrates the channel-wise transformation used by
    the framework without exposing the complete data pipeline or model wiring.
    """

    def __init__(self, d_model: int, d_inner: int, dropout: float = 0.1):
        super().__init__()
        self.norm = nn.LayerNorm(d_model)
        self.key = nn.Linear(d_model, d_inner, bias=False)
        self.value = nn.Linear(d_inner, d_model, bias=False)
        self.gate = nn.Linear(d_model, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        residual = x
        x = self.norm(x)
        hidden = torch.square(F.relu(self.key(x)))
        mixed = torch.sigmoid(self.gate(x)) * self.value(hidden)
        return residual + self.dropout(mixed)


class CommunityFeatureAdapter(nn.Module):
    """Accept externally prepared community features.

    The community detection and assignment-generation procedure is outside
    the scope of this partial public release.
    """

    def __init__(self, entity_dim: int, community_dim: int, output_dim: int):
        super().__init__()
        self.projection = nn.Linear(entity_dim + community_dim, output_dim)

    def forward(self, entity_features: torch.Tensor,
                community_features: torch.Tensor) -> torch.Tensor:
        features = torch.cat((entity_features, community_features), dim=-1)
        return self.projection(features)
