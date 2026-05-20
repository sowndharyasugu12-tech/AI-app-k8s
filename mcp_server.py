from mcp.server.fastmcp import FastMCP
from tools.k8s_tool import get_pods

mcp = FastMCP("DevOps-MCP")


@mcp.tool()
def get_running_pods():
    return {"running_pods": get_pods()}
