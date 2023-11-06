import asyncio
from bleak import BleakScanner


async def main():
    stop_event = asyncio.Event()
    print(f'\r{"=" * 30}')
    oldDevices = 0
    OUI = '00:25:DF'
    devices = []
    foundWithName = []
    # TODO: add something that calls stop_event.set()

    def callback(device, advertising_data):
        # print(device)
        # print(advertising_data)
        nonlocal oldDevices
        if device.address not in devices:
            devices.append(device.address)
            if OUI in device.address[:8]:
                print(f'\rDevice Address:  {device.address}')
                print(f'\rSignal Strength: {advertising_data.rssi}')
                print(f'\rManufacturer:    Taser International')
                if device.name:
                    print(f'\rDevice Name:     {device.name}')
                    foundWithName.append(device.address)
                print(f'\r{"=" * 30}')

        if len(devices) != oldDevices:
            print(f'\r{len(devices)}', end='')
            oldDevices = len(devices)
        pass

    async with BleakScanner(callback, scanning_mode='passive') as scanner:
        ...
        # Important! Wait for an event to trigger stop, otherwise scanner
        # will stop immediately.
        await stop_event.wait()

    # scanner stops when block exits
    ...

asyncio.run(main())
