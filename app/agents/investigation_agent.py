from agentspan.agents import Agent, tool

# --- MONKEY PATCH START ---
# Fixes a bug in agentspan where Conductor worker fails to inject `task` due to a string type hint.
try:
    from agentspan.agents.runtime._dispatch import ToolWorkerCallable
    if hasattr(ToolWorkerCallable.__call__, "__annotations__"):
        ToolWorkerCallable.__call__.__annotations__.pop("task", None)
except ImportError:
    pass
# --- MONKEY PATCH END ---

@tool
def get_user_by_id(user_id: str) -> dict:
    """
    Look up a user by user_id in the MySQL users table.
    """
    from app.tools.user_tools import get_user_by_id as lookup_user

    return lookup_user(user_id)


@tool
def find_user_exceptions(user_id: str) -> dict:
    """
    Find all exception logs associated with a specific user.
    """
    from app.tools.exception_tools import (
        find_user_exceptions as find_exceptions,
    )

    return find_exceptions(user_id)


@tool
def read_exception_log(filename: str) -> dict:
    """
    Read the complete contents of a specific exception log.
    """
    from app.tools.exception_tools import (
        read_exception_log as read_log,
    )

    return read_log(filename)


investigation_agent = Agent(
    name="order_investigation_agent",

    model="google_gemini/gemini-3-flash-preview",

    instructions="""
You are an e-commerce incident investigation agent.

Your job is to investigate whether a specific user was affected
by an application/system failure.

Investigation process:

1. Look up the user using get_user_by_id.
2. If the user does not exist, report that clearly.
3. Search for exception logs associated with the user using
   find_user_exceptions.
4. If exceptions are found, read the relevant logs using
   read_exception_log.
5. Analyze the evidence.
6. Determine:
   - whether the user appears to be affected
   - what failures occurred
   - which services were involved
   - severity
   - whether multiple failures may be related
7. Never invent information.
8. Base conclusions only on information returned by tools.

Return a concise investigation report.
""",

    tools=[
        get_user_by_id,
        find_user_exceptions,
        read_exception_log,
    ],

    max_turns=10,
)