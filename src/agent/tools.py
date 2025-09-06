from agents import function_tool

@function_tool
def print_okay() -> str:
    """Simple tool that prints 'okay' and returns it."""
    print("okay")
    return "okay"