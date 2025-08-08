import pandas as pd
import io
import base64
import matplotlib.pyplot as plt
import numpy as np

def read_csv(fileobj):
    return pd.read_csv(fileobj)

def scatter_with_regression(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    m, b = np.polyfit(x, y, 1)
    ax.plot(x, m*x + b, 'r--', label='Regression line')
    ax.set_xlabel('Rank')
    ax.set_ylabel('Peak')
    ax.legend()
    fig.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"
