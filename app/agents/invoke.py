from agentspan.agents import AgentRuntime

from app.agents.investigation_agent import investigation_agent


def main():
    prompt = """
    Investigate user USR-10001.

    Determine whether this user was affected by an application failure.

    Identify:
    - the affected user
    - all relevant exceptions
    - services involved
    - severity
    - likely relationship between the failures

    Base your conclusion only on evidence returned by the tools.
    """

    with AgentRuntime(
        server_url="http://localhost:6767/api",
    ) as runtime:

        result = runtime.run(
            investigation_agent,
            prompt,
        )

        result.print_result()


if __name__ == "__main__":
    main()