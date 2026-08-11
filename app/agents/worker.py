from agentspan.agents import AgentRuntime

from app.agents.investigation_agent import investigation_agent


def main():
    with AgentRuntime(
        server_url="http://localhost:6767/api",
    ) as runtime:

        print("Starting AgentSpan workers...")

        runtime.serve(
            investigation_agent,
            blocking=True,
        )


if __name__ == "__main__":
    main()