import torch
from torch import nn


class CustomTransformerEncoderLayer(nn.Module):
    def __init__(self, d_model=1024, nhead=1600, dim_feedforward=204800, dropout=0.1):
        """
        Custom Transformer Encoder Layer.

        Parameters
        ----------
        d_model : int
        nhead : int
        dim_feedforward : int
        dropout : float
        """
        super(CustomTransformerEncoderLayer, self).__init__()

        self.self_attn = nn.MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=True)

        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, d_model)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

        self.activation = nn.ReLU()

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        """
        Forward pass.

        Parameters
        ----------
        src : torch.Tensor
        src_mask : torch.Tensor
        src_key_padding_mask : torch.Tensor

        Returns
        -------
        torch.Tensor
        """
        src2 = self.self_attn(src, src, src, attn_mask=src_mask,
                              key_padding_mask=src_key_padding_mask)[0]
        src = src + self.dropout1(src2)
        src = self.norm1(src)
        src2 = self.linear2(self.dropout(self.activation(self.linear1(src))))
        src = src + self.dropout2(src2)
        src = self.norm2(src)

        return src


class AGI(nn.Module):
    def __init__(self, input_dim=1024, num_heads=160, num_layers=120):
        """
        AGI model.

        Parameters
        ----------
        input_dim : int
        num_heads : int
        num_layers : int
        """
        super(AGI, self).__init__()
        self.encoder = nn.TransformerEncoder(
            CustomTransformerEncoderLayer(d_model=input_dim, nhead=num_heads), num_layers=num_layers
        )

    def forward(self, src):
        """
        Forward pass.

        Parameters
        ----------
        src : torch.Tensor

        Returns
        -------
        torch.Tensor
        """
        output = self.encoder(src)

        return output
