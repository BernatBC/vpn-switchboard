from app.core.providers.cloudflare_warp import warp_setup

def setup_vpn(args):
    """Sets up a specified VPN configuration."""
    vpn_name = getattr(args, 'vpn_name', None)
    if not vpn_name:
        print("Error: VPN name not specified for setup command.")
        return
    if vpn_name == "warp":
        warp_setup()