from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({
    "devops": {
        "command": "python",
        "args": ["mcp_server.py"],
        "transport": "stdio"
    }
})


def ask_agent(query):

    q = query.lower()

    # 🔥 FORCE TOOL ROUTING
    if "pod" in q:
        return client.invoke({
            "input": "get_running_pods"
        })

    return client.invoke({"input": query})
