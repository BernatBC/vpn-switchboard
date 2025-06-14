from app.core.providers.cloudflare_warp import warp_disconnect

def disconnect_vpn(args):
    """Disconnects from the current or a specified VPN."""
    vpn_name = getattr(args, 'vpn_name', None)
    if not vpn_name:
        print("Error: VPN name not specified for disconnect command.")
        return
    if vpn_name == "warp":
        warp_disconnect()