from agentspan.agents import AgentRuntime

from app.agents.investigation_agent import investigation_agent


def main():
    prompt = """
    Investigate user USR-10001.

    Determine whether this user was affected by an application failure.
    Identify the relevant exceptions and explain what happened.
    """

    with AgentRuntime(
        server_url="http://localhost:6767/api",
    ) as runtime:

        result = runtime.run(
            investigation_agent,
            prompt,
        )

        print("Result:")
        result.print_result()


if __name__ == "__main__":
    main()