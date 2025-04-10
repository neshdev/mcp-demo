import kagglehub.datasets
from mcp.server.fastmcp import FastMCP
import logging
logging.basicConfig(level=logging.DEBUG)

import pandas as pd
import matplotlib.pyplot as plt
import io

import os
os.environ["KAGGLE_KEY"] = "5755c005db636cf7c05da4c5e6a85e10"
os.environ["KAGGLE_USERNAME"] = "neshdev"

import kagglehub

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import io

import re

api = KaggleApi()
api.authenticate()
# print(api.model_list())

# Create an MCP server
mcp = FastMCP("Demo")

mcp.add_tool(api.dataset_list)

def todoc(contents):
    c = contents[0:64]
    c = re.sub(r"[^a-zA-Z0-9_-]", " ")
    return c

mcp.add_tool(kagglehub.dataset_download, description=kagglehub.dataset_download.__doc__)

@mcp.tool()
def dataset_analyze(handle:str, path: str, x, y, kind='scatter') -> PILImage:
    """
    Analyze the dataset with pandas.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        x (str): Column name for x-axis.
        y (str): Column name for y-axis.
        kind (str): Type of plot (e.g., 'scatter', 'line').
        **plot_kwargs: Additional keyword arguments passed to DataFrame.plot().
    
    Returns:
        PIL.Image.Image: The plot rendered as a PIL image.
    """
    df = kagglehub.datasets.dataset_load(handle=handle, path=path)
    fig, ax = plt.subplots()
    df.plot(kind=kind, x=x, y=y, ax=ax)
    plt.title(f"{kind.capitalize()} Plot of {y} vs {x}")

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)

    img = PILImage.open(buf)
    img.load()
    buf.close()

    return img

if __name__ == "__main__":
    mcp.run()