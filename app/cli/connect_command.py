from app.core.providers.cloudflare_warp import warp_connect

def connect_vpn(args):
    """Connects to a specified VPN."""
    vpn_name = getattr(args, 'vpn_name', None)
    if not vpn_name:
        print("Error: VPN name not specified for connect command.")
        return
    if vpn_name == "warp":
        warp_connect()