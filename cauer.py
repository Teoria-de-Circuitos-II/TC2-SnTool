import scipy.special
import scipyx as scx
import numpy as np
import plotly.graph_objs as go

class Cauer:
    def __init__(self, k= None):
        self.k = k
        
        self.maxLi = self.Li_SN(0.001)
        self.maxL = self.L_SN(0.999)

    def SenoEliptico(self, z, k):
        sn, cn, dn, ph = scx.ellipj(u=z, m=k**2)
        return sn

    def L_SN(self, k):
        return float(np.real(scipy.special.ellipk(k**2)))

    def Li_SN(self, k):
        return float(scipy.special.ellipk(1 - k**2))
    
    def config_figure(self, z, L, Li):
        zeros = np.array([[{"re": 2*n*L, "im": 2*i*Li} for n in range(-20, 20)] for i in range(-10, 10)]).flatten()
        poles = np.array([[{"re": 2*n*L, "im": (2*i-1)*Li} for n in range(-20, 20)] for i in range(-10, 10)]).flatten()
        
        xlim = max([abs(z.real), 2*self.maxL])*1.4
        xlims = [-xlim, xlim]
        if(z.imag < -self.maxLi/5):
            ylims = [z.imag, self.maxLi]
        elif(z.imag > self.maxLi):
            ylims = [-z.imag, z.imag]
        else:
            ylims = [-self.maxLi/5, self.maxLi]
        ylims[0] *= 1.4
        ylims[1] *= 1.4

        fig = go.Figure()
        fig.update_layout(
            xaxis_title="Real",
            yaxis_title="Imaginary",
            width=400, height=300,
            showlegend=False
        )
        
        fig.update_layout(
            xaxis=dict(title="Real", range=xlims, showgrid=False),
            yaxis=dict(title="Imaginary", range=ylims, showgrid=False),
        )
        fig.update_layout(
            shapes=[
                dict(
                    type="line",
                    x0=0, x1=0,
                    y0=-1000, y1=1000,  # Match your y-axis range
                    line=dict(color="#31333f", width=1)
                ),
                dict(
                    type="line",
                    x0=-1000, x1=1000,
                    y0=0, y1=0,
                    line=dict(color="#31333f", width=1)
                ),
                dict(
                    type="line",
                    x0=0, x1=L,
                    y0=0, y1=0,
                    line=dict(color="#d62728", width=1, dash="dot")
                ),
                dict(
                    type="line",
                    x0=L, x1=L,
                    y0=0, y1=Li,
                    line=dict(color="#d62728", width=1, dash="dot")
                ),
                dict(
                    type="line",
                    x0=L, x1=0,
                    y0=Li, y1=Li,
                    line=dict(color="#d62728", width=1, dash="dot")
                ),
                dict(
                    type="line",
                    x0=0, x1=-L,
                    y0=0, y1=0,
                    line=dict(color="#9467bd", width=1, dash="dot")
                ),
                dict(
                    type="line",
                    x0=-L, x1=-L,
                    y0=0, y1=Li,
                    line=dict(color="#9467bd", width=1, dash="dot")
                ),
                dict(
                    type="line",
                    x0=-L, x1=0,
                    y0=Li, y1=Li,
                    line=dict(color="#9467bd", width=1, dash="dot")
                ),
            ]
        )
        fig.add_trace(go.Scatter(
            x=[z["re"] for z in zeros],
            y=[z["im"] for z in zeros],
            mode="markers",
            marker=dict(symbol="circle", size=12, color="#1f77b4"),
            name="zeros"
        ))
        fig.add_trace(go.Scatter(
            x=[p["re"] for p in poles],
            y=[p["im"] for p in poles],
            mode="markers",
            marker=dict(symbol="x-thin", size=12, color="red", line_width=2, line_color='#ff7f0e'),
            name="poles"
        ))
        fig.add_trace(go.Scatter(
            x=[z.real],
            y=[z.imag],
            mode="markers",
            marker=dict(symbol="diamond", size=10, color="#2ca02c"),
            name="point"
        ))
        
        fig.update_layout(
            margin=dict(l=10, r=10, t=5, b=10)
        )

        return fig