from app.core.run_bash_command import run_bash_command, BashCommandStatus
from app.core.vpn_configurations import add_configuration, remove_configuration, is_configured

CONFIGURATION_NAME = "warp"

def warp_setup():
    """
    Setup function for Cloudflare Warp VPN.
    This function is called when the user runs the 'setup' command for Cloudflare Warp.
    """
    if (is_configured(CONFIGURATION_NAME)):
        print("Already configured")
        return
    print("Setting up Cloudflare Warp VPN...")
    
    add_configuration(CONFIGURATION_NAME)

def warp_connect():
    """
    Connect function for Cloudflare Warp VPN.
    This function is called when the user runs the 'connect' command for Cloudflare Warp.
    """
    if (not is_configured(CONFIGURATION_NAME)):
        print("Not configured")
        print("Run: vpn-switchboard setup " + CONFIGURATION_NAME)
        return
    (code, output) = run_bash_command("warp-cli connect")
    if code == BashCommandStatus.SUCCESS:
        if output == "Success":
            print("Cloudflare Warp VPN connected successfully.")
        else:
            print(f"Failed to connect Cloudflare Warp VPN: {output}")
            return
    elif code == BashCommandStatus.ERROR_COMMAND_FAILED:
        print(f"Failed to connect Cloudflare Warp VPN: {output}")
        return
    elif code == BashCommandStatus.ERROR_COMMAND_NOT_FOUND:
        print(f"Command not found: {output}")
        return

def warp_disconnect():
    """
    Disconnect function for Cloudflare Warp VPN.
    This function is called when the user runs the 'disconnect' command for Cloudflare Warp.
    """
    if (not is_configured(CONFIGURATION_NAME)):
        print("Not configured")
        print("Run: vpn-switchboard setup " + CONFIGURATION_NAME)
        return
    (code, output) = run_bash_command("warp-cli disconnect")
    if code == BashCommandStatus.SUCCESS:
        if output == "Success":
            print("Cloudflare Warp VPN disconnected successfully.")
        else:
            print(f"Failed to disconnect Cloudflare Warp VPN: {output}")
            return
    elif code == BashCommandStatus.ERROR_COMMAND_FAILED:
        print(f"Failed to disconnect Cloudflare Warp VPN: {output}")
        return
    elif code == BashCommandStatus.ERROR_COMMAND_NOT_FOUND:
        print(f"Command not found: {output}")
        return

def warp_remove():
    """
    Remove function for Cloudflare Warp VPN.
    This function is called when the user runs the 'remove' command for Cloudflare Warp.
    """
    if (not is_configured(CONFIGURATION_NAME)):
        print("Not configured")
        return
    print("Removing Cloudflare Warp VPN configuration...")

    remove_configuration("warp")