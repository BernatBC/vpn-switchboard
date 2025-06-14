def disconnect_vpn(args):
    """Disconnects from the current or a specified VPN."""
    vpn_name = getattr(args, 'vpn_name', None)
    if vpn_name:
        print(f"Disconnecting from VPN: {vpn_name}...")
    else:
        print("Disconnecting from current VPN...")
    # Placeholder for actual disconnection logic