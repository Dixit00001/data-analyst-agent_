import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

def read_csv(fileobj):
    return pd.read_csv(fileobj)

def scatter_with_regression(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # Regression line via polyfit
    m, b = pd.np.polyfit(x, y, 1)
    ax.plot(x, m*x + b, 'r--', label='Regression')
    ax.set_xlabel("Rank")
    ax.set_ylabel("Peak")
    ax.legend()
    fig.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    buf.seek(0)
    img_bytes = buf.read()
    return "data:image/png;base64," + base64.b64encode(img_bytes).decode()

