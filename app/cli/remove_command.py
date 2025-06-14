from app.core.providers.cloudflare_warp import warp_remove

def remove_vpn(args):
    """Removes a specified VPN configuration."""
    vpn_name = getattr(args, 'vpn_name', None)
    if not vpn_name:
        print("Error: VPN name not specified for remove command.")
        return
    if vpn_name == "warp":
        warp_remove()